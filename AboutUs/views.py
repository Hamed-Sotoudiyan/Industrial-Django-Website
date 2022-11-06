from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def MissionStatement(request):
    return render(request, 'AboutUs/MissionStatement.html')

def Structure(request):
    return render(request, 'AboutUs/Structure.html')
