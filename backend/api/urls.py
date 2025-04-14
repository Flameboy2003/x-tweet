from django.urls import path
from .views import search_tweets


urlpatterns = [
     path('tweets/', search_tweets), 
]
