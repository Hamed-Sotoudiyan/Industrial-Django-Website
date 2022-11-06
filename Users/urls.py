from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [
    path('login/', views.LoginFunction, name='LoginFunction'),
    path('profile/', views.Profile, name='Profile'),
]
