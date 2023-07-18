# chat/urls.py
from django.urls import path

from .views import homePageView, get_chatroom_html,add_message, create_chatroom

app_name = 'chat'
urlpatterns = [
    path("", homePageView, name="home"),
    path('get_chatroom_messages/', get_chatroom_html, name='get_chatroom_html'),
    path('add_message/', add_message, name='add_message'),
    path('create_chatroom/', create_chatroom, name='create_chatroom'),
]