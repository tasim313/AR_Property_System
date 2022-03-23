from django import forms
from App_Add_Flat.models import Add_Flat, Update_Rent

class Add_FlatForm(forms.ModelForm):
    class Meta:
        model = Add_Flat
        fields = '__all__'

class Update_rent_Form(forms.ModelForm):
    class Meta:
        model = Update_Rent
        fields = '__all__'

