from django.urls import path
from App_Feedback import views

app_name = 'App_Feedback'

urlpatterns = [
     path('addfeedback/', views.user_feedback, name='add_feedback'),
]