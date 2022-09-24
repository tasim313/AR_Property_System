from django.db import models
from App_Login.models import CreateUser

# Create your models here.


class Feedback(models.Model):
    user = models.ForeignKey(CreateUser, related_name='user_feedback', on_delete=models.CASCADE)
    house_name = models.CharField(max_length=200, blank=True)
    flat_number = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=300, blank=True)
    feedback = models.TextField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User{self.user}+House Name{self.house_name}+Flat Number{self.flat_number}'


class Replay_Feedback(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='reply_feedback')
    replay_feedback = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.replay_feedback

