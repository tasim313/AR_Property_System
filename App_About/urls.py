from django.urls import path
from App_About import views
app_name = 'App_About'

urlpatterns = [
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
]
