from django.urls import path
from . import views

app_name = 'Customers'

urlpatterns = [
    path('', views.Customers, name='Customers'),
]
