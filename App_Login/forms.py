# Import forms
from django.forms import ModelForm
from django import forms
# Import Model
from django import forms
from App_Login.models import user_registration
from django.contrib.auth.forms import UserCreationForm
from App_Login.models import CreateUser


class CreatUserForm(UserCreationForm):
    class Meta:
        model = CreateUser
        fields = ['email', 'password1', 'password2', 'is_renter', 'is_owner']


class LoginForm(forms.Form):
    email = forms.EmailField(
     widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class User_Registration_Form(forms.ModelForm):
    class Meta:
        model = user_registration
        exclude = ['user']

