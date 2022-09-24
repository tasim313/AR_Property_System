from django.shortcuts import render

# Create your views here.
def About(request):
    diction = {'about': 'about'}
    return render(request, 'App_About/about.html', context=diction)

def Contact(request):
    diction = {'contact': 'contact'}
    return render(request, 'App_About/Contact.html', context=diction)
