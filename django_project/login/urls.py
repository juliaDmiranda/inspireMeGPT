# login/urls.py
from django.urls import path

from .views import loginPageView

app_name = 'login'

urlpatterns = [
    path("", loginPageView, name="login"),
]