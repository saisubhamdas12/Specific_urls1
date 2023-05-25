from django.urls import path
from app1.views import*
app_name='run'
urlpatterns =  [
    path('virat/',virat,name='virat'),
]