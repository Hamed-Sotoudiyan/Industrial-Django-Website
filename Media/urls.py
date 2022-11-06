from django.urls import path
from . import views

app_name = 'Media'

urlpatterns = [
    path('', views.Media, name='Media'),
]
