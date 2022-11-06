from django.urls import path
from . import views

app_name = 'Gallery'

urlpatterns = [
    path('', views.Gallery, name='Gallery'),
]
