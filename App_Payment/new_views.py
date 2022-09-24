from django.shortcuts import render

from .models import *
from .forms import *


def billinginfo(request):
    form = BillingForm()
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Complete Billing Info')
            return HttpResponseRedirect(reverse('home'))
    diction = {'form': form}
    return render(request, 'App_Payment/billing.html', context=diction)
