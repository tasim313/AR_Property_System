from django.urls import path
from App_Add_Flat import views

app_name = 'App_Add_Flat'

urlpatterns = [
    path('addflat/', views.add_flat, name='add_flat'),
    path('details/<pk>/', views.product_Details.as_view(), name='product_details'),
    path('user_list/', views.User_list.as_view(), name='user_list'),
]
