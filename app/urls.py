from django.urls import path
from app.views import*
app_name="best"

urlpatterns=[
    path('msd/',msd,name='msd'),
]