import stripe
from django.shortcuts import redirect, render
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

from .api import (
    update_stripe_customer_api,
    user_information_api
)


def product_plan(request):
    # get session data
    session_user_data = request.session.get('user_data')
    # print("product_plan(): session_user_data",
    #       session_user_data['stripe_user_id'])

    # get stripe ucstomer from session user_data
    # stripe_customer_id = session_user_data['stripe_user_id']

    all_products = stripe.Product.list()
    print("Products", all_products)
    price_list = stripe.Price.list()
    print("Price", price_list)

    count = 1
    active_products = []
    for count in range(0, len(all_products)+1):
        for product in all_products:
            if product['active'] == True:
                if int(product['metadata']['counter']) == count:
                    active_products.append(product)
        count += 1
    print('tttttttttttt', active_products)

    for active_product in active_products:
        for price in price_list:
            product_prices = [
                price for price in price_list if price['product'] == active_product['id']]
        active_product['prices'] = product_prices

    # product_price_list = [
    #     price for price in price_list if price['product'] == 'prod_I8PIVDmzdhbw7f']

    # print('active_products', active_products)

    context = {
        "active_products": active_products,
    }

    return render(request, 'App_Payment/product_plan.html', context)


def add_card_view(request):
    try:
        if request.POST:
            card_number = request.POST.get('card_number')
            print(card_number)
            exp_date_month = request.POST.get('exp_date_month')
            print(exp_date_month)
            exp_date_year = request.POST.get('exp_date_year')
            print(exp_date_year)
            cvc = request.POST.get('cvc')
            print(cvc)
            user_data = request.session.get('user_data')
            user_stripe_id = user_data['stripe_user_id']
            print("user_data", user_data)
            print("user_stripe_id", user_stripe_id)

            # create payment method for customer
            payment_method = stripe.PaymentMethod.create(
                type="card",
                card={
                    "number": card_number,
                    "exp_month": exp_date_month,
                    "exp_year": exp_date_year,
                    "cvc": cvc,
                },
            )
            print('add_card_view(): payment_method', payment_method)

            if payment_method["id"]:
                payment_method_id = payment_method["id"]
                attach_payment_method = stripe.PaymentMethod.attach(
                    str(payment_method_id),
                    customer=str(user_stripe_id),
                )

                attach_payment_method = stripe.Customer.modify(
                    str(user_stripe_id),
                    invoice_settings={
                        "default_payment_method": str(payment_method_id)},
                )

                print("add_card_view(): attach_payment_method", attach_payment_method)
                return redirect('mi_payments:product_price')
            else:
                messages.error(request, "Please try again")
    except Exception as Ex:
        print("add_card_view(): Ex", Ex)
        messages.error(request, "Please try again")

    return render(request, 'App_Payment/card.html')


def create_suscription(request, price_id, customer_id, product_id):
    session_user_data = request.session.get('user_data')
    print("create_suscription(): session_user_data",
          session_user_data['stripe_subscription_id'])

    # get stripe ucstomer from session user_data
    stripe_subscription_id = session_user_data['stripe_subscription_id']
    user_id = session_user_data['id']
    stripe_customer_id = session_user_data['stripe_user_id']

    # suscription = stripe.Subscription.create(
    #     customer=str(customer_id),
    #     items=[
    #         {"price": str(price_id)},
    #     ],
    # )

    subscription = stripe.Subscription.retrieve(stripe_subscription_id)

    stripe_product_id = subscription["items"]['data'][0]['price']['product']
    print("create_suscription(): user stripe_product_id from stripe", stripe_product_id)

    if product_id != stripe_product_id:

        try:

            upgrade_subscription = stripe.Subscription.modify(
                subscription.id,
                cancel_at_period_end=False,
                proration_behavior='create_prorations',
                items=[{
                    'id': subscription['items']['data'][0].id,
                    'price': str(price_id),
                }]
            )

            print("create_suscription(): upgrade_subscription", upgrade_subscription)

            stripe_product_id = upgrade_subscription["items"]['data'][0]['price']['product']
            print('create_suscription(): stripe_product_id', stripe_product_id)

            # update user with stripe customer id
            update_user = update_stripe_customer_api(
                user_id=str(user_id),
                stripe_user_id=str(stripe_customer_id),
                stripe_subscription_id=str(subscription.id),
                stripe_product_id=str(stripe_product_id),
            )

            print('create_suscription(): update_user', update_user)

            # save stripe meta data is the user has a subcription
            stripe_product_id = str(
                upgrade_subscription["items"]['data'][0]['price']['product'])
            customer_plan = stripe.Product.retrieve(
                str(stripe_product_id))
            print('create_suscription() :customer_plan', customer_plan)
            plan_metadata = customer_plan['metadata']
            print('create_suscription() :plan_metadata', plan_metadata)

            # set plan metadata in session
            # del request.session['plan_metadata']
            request.session['plan_metadata'] = plan_metadata

            auth_token = request.session.get('auth_token')

            # get user information from user account management
            user = user_information_api(
                token=auth_token
            )
            if bool(settings.DEBUG): print('create_suscription(): user data from user dashboard', user.json())

            # set session in user_data
            request.session['user_data'] = user.json()
            user_data = request.session['user_data']
            if bool(settings.DEBUG): print('create_suscription(): session user_data', user_data)

            # Set session as modified to force data updates/cookie to be saved.
            request.session.modified = True

            print('create_suscription() :session customer_plan',
                  request.session.get('plan_metadata'))

            return JsonResponse(data={"Success": True, "suscription": upgrade_subscription}, safe=False)
        except Exception as ex:
            return JsonResponse(data={"Success": False, "ex": ex}, safe=False)
    else:
        print('create_suscription() You are already subscribed in this plan')
        return JsonResponse(data={"Success": False, "ex": "You are already subscribed in this plan."}, safe=False)


def subcription_plan_details(request):
    # get session data from user data
    session_user_data = request.session.get('user_data')
    print("subcription_plan_details(): stripe_product_id",
          session_user_data['stripe_product_id'])

    # get sstripe_product_id from session user_data
    stripe_product_id = session_user_data['stripe_product_id']

    # get the customer current plan from stripe
    current_plan = stripe.Product.retrieve(str(stripe_product_id))
    print('subcription_plan_details() :customer_plan', current_plan)

    return JsonResponse(data={"Success": True, "current_plan": current_plan}, safe=False)


def check_customer_card_information(request):
    # get session data
    session_user_data = request.session.get('user_data')
    print("product_plan(): session_user_data",
          session_user_data['stripe_user_id'])
    print("product_plan(): session_user_data",
          session_user_data)

    # get stripe ucstomer from session user_data
    stripe_customer_id = session_user_data['stripe_user_id']

    check_customer_card = stripe.PaymentMethod.list(
        customer=stripe_customer_id,
        type="card",
    )

    if check_customer_card['data']:
        data = {
            "Success": True,
            "current_plan": check_customer_card
        }
    else:
        data = {
            "Success": False,
            "current_plan": check_customer_card
        }

    return JsonResponse(data={"data": data}, safe=False)


def get_card_info_list(request):
    session_user_data = request.session.get('user_data')
    stripe_customer_id = session_user_data['stripe_user_id']

    return JsonResponse(data={"data": stripe.PaymentMethod.list(
        customer=stripe_customer_id,
        type="card",
    )}, safe=False)