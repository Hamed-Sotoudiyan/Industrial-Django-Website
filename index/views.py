from django.shortcuts import render
import requests
import json
import re
from bs4 import BeautifulSoup


# Create your views here.
def home(request):

    context={}
    return render(request, 'index/index.html', context)
