from django.urls import path
from WeatherAPI.views import *
urlpatterns =[
    path('weather/',get_weather)
]