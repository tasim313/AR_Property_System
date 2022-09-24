from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
# Import views
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# import models and Form
from App_Add_Flat.models import Add_Flat
from App_Add_Flat.forms import Add_FlatForm

# Messages
from django.contrib import messages


# model import
from App_Login.models import CreateUser
from App_Flat_Booking.models import Booking

# Create your views here.


class Home(ListView):
    context_object_name = 'object_list'
    model = Add_Flat
    template_name = 'home.html'


def add_flat(request):
    form = Add_FlatForm()
    if request.method == 'POST':
        form = Add_FlatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Add  Flat')
            return HttpResponseRedirect(reverse('home'))
    diction = {'form': form}
    return render(request, 'App_Add_Flat/add_flat.html', context=diction)


class product_Details(LoginRequiredMixin, DetailView):
    context_object_name = 'details'
    model = Add_Flat
    template_name = 'App_Add_Flat/flat_details.html'


class User_list(LoginRequiredMixin, ListView):
    context_object_name = 'user_list'
    model = CreateUser  # here the model will be add_flat cz customer will be relation with flat by booking flat
    template_name = 'App_Add_Flat/renter_list.html'


