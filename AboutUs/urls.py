from django.urls import path
from . import views

app_name = 'AboutUs'

urlpatterns = [
    path('missionstatement/', views.MissionStatement, name='MissionStatement'),
    path('structure/', views.Structure, name='Structure'),

]
