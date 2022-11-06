from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def ContactUs(request):
    return render(request, 'ContactUs/ContactUs.html')
