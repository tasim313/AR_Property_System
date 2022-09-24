from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def user_feedback(request):
    user = request.user
    form = Feedback_Form(instance=user)
    if request.method == 'POST':
        form = Feedback_Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Add  FeedBack')
            return HttpResponseRedirect(reverse('home'))
    diction = {'form': form}
    return render(request, 'App_FeedBack/feedback.html', context=diction)
