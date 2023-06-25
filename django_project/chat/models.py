from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat Room: {self.chat_room}, Sender: {self.sender.username}, Message: {self.message}"