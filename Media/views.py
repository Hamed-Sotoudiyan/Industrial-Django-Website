from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Media(request):
    return render(request, 'Media/Media.html')
