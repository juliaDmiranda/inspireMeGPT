# singup/urls.py
from django.urls import path

from .views import signupPageView

app_name = 'signup'

urlpatterns = [
    path("", signupPageView, name="signup"),
]