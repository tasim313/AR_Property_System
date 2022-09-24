from App_Feedback.models import Feedback, Replay_Feedback
from django import forms
from django.forms import ModelForm


class Feedback_Form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['house_name', 'flat_number', 'address', 'feedback']


class Replay_Form(forms.ModelForm):
    class Meta:
        model = Replay_Feedback
        fields = ['replay_feedback']
        