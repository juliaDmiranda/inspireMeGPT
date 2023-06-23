# chat/urls.py
from django.urls import path

from .views import homePageView

app_name = 'chat'
urlpatterns = [
    path("", homePageView, name="home"),
]