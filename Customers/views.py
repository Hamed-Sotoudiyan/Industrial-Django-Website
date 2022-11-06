from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Customers(request):
    return render(request, 'Customers/Customers.html')
