from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# import models and Form
from App_Add_Flat.models import Add_Flat
from App_Add_Flat.forms import Add_FlatForm

# Messages
from django.contrib import messages


# Create your views here.
def add_flat(request):
    form = Add_FlatForm()
    if request.method == 'POST':
        form = Add_FlatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Add  Flat')
            return HttpResponseRedirect(reverse('App_Login:home'))
    diction = {'form': form}
    return render(request, 'App_Add_Flat/add_flat.html', context=diction)
