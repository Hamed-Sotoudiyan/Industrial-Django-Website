from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Gallery(request):
    return render(request, 'Gallery/Gallery.html')
