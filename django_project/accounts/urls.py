# login/urls.py
from django.urls import path
from .views import loginPageView,logoutPageView, signupPageView,activate,account_activation_sent
from django.views.generic import RedirectView
app_name = 'accounts'

urlpatterns = [
    path("login/", loginPageView, name="login"),
    path("", logoutPageView, name="logout"),
    path("signup/", signupPageView, name="signup"),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    # path('login/', loginPageView, name="login"),
    path('accounts/login/', loginPageView, name='login'),
    # path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate, name='activate'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
]