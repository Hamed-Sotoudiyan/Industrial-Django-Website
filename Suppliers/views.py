from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Suppliers(request):
    return render(request, 'Suppliers/Suppliers.html')
