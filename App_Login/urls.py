from django.urls import path
from App_Login import views
app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/', views.registrationform, name='registration'),
    path('user_profile/', views.User_profile, name='user_profile'),
    path('search/', views.searchbar, name='search'),
]

