# myapi/urls.py

from django.urls import include, path
from rest_framework import routers
from .views import TweetView,UserView

app_name = "tweets"

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('tweets/', TweetView.as_view()),
    path('users/', UserView.as_view()),
    path('tweets/<int:pk>', TweetView.as_view())
]