from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
def index(request):
    
    return render(
        request,
        'index.html',
        context={},
    )
def about(request):
    
    return render(
        request,
        'about.html',
        context={},
    ) 

def contact(request):
    
    return render(
        request,
        'contact.html',
        context={},
    )    