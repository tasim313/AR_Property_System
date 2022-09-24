import os
# from django.http import response
from django.http import response
import requests
from requests.api import request
# from requests.api import request
from requests.exceptions import HTTPError
from django.conf import settings

BASE_URL = "http://127.0.0.1:8000/"


AUTHENTICATION_URL = "http://127.0.0.1:8000/"
# create customer instance in redish


def update_stripe_customer_api(**args):
    try:
        url = AUTHENTICATION_URL + \
            "/accounts/update-stripe-c-id/" + args['user_id'] + "/"
        # user_id = str(args['user_id'])
        response = requests.put(
            url,
            headers={
                "Content-Type": "application/json",
            },
            json={
                # "id": user_id,
                "stripe_user_id": args['stripe_user_id'],
                "stripe_subscription_id": args['stripe_subscription_id'],
                "stripe_product_id": args['stripe_product_id']
            }
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'update_stripe_customer_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'update_stripe_customer_api(): Other error occurred: {err}')
    else:
        print('update_stripe_customer_api(): Success!')

    return response


def user_information_api(**args):
    """
    get the informatioon of login user
    """
    try:
        me_url = AUTHENTICATION_URL + "/auth/users/me"
        token = args['token']

        response = requests.get(
            me_url,
            headers={
                "Content-Type": "application/json",
                "Authorization": 'Token' + ' ' + token
            }
        )

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'user_information_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'user_information_api(): Other error occurred: {err}')
    else:
        print('user_information_api(): Success!')

    return response