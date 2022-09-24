from django.urls import path, include
from . import views
from . import stripeviews, new_views
app_name = 'App_Payment'

urlpatterns = [
     # path('checkout/', views.checkout, name='CheckOut'),
     # path('pay/', views.payment, name='payment'),
     # path('status/', views.complete, name='complete'),
     # path('purchase/<val_id>/<tran_id>/', views.purchase, name="purchase"),
     # path('orders/', views.order_view, name="orders"),
     # ######### new url ############
     # path('', stripeviews.product_plan, name='product_price'),
     # path('add_card', stripeviews.add_card_view, name='add_card'),
     # path('create-mi-suscription/<price_id>/<customer_id>/<product_id>/',
     #     stripeviews.create_suscription, name='create_mi_suscription'),
     # path('subcription_plan_details/',
     #     stripeviews.subcription_plan_details, name='subcription_plan_details'),
     # path('check-customer-card-information/', stripeviews.check_customer_card_information, name='check_customer_card_information'),
     #
     # path('get_card_info_list/', stripeviews.get_card_info_list, name='get_card_info_list'),
     #
     # path("stripe/", include("djstripe.urls", namespace="djstripe")),
     # path("checkout", new_views.checkout, name="checkout"),
     # path("create-sub", new_views.create_sub, name="create sub"),
     # path("complete", new_views.complete, name="complete"),
     # path("cancel", new_views.cancel, name="cancel"),
    path("bill/", new_views.billinginfo, name='bill'),
]