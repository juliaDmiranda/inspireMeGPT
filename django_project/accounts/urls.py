from django.urls import path
from .views import loginPageView,logoutPageView, signupPageView,activate,account_activation_sent
from django.views.generic import RedirectView
app_name = 'accounts'

urlpatterns = [
    path("login/", loginPageView, name="login"),
    path("", logoutPageView, name="logout"),
    path("signup/", signupPageView, name="signup"),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    path('accounts/login/', loginPageView, name='login'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
]