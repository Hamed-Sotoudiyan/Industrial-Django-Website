from django.urls import path
from . import views

app_name = 'ContactUs'

urlpatterns = [
    path('', views.ContactUs, name='ContactUs'),
]
