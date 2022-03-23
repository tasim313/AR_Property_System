from django.urls import path
from App_Add_Flat import views

app_name = 'App_Add_Flat'

urlpatterns = [
    path('addflat/', views.add_flat, name='add_flat'),

]
