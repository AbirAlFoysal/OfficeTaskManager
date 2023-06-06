from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class Chat(models.Model):
    friend = User.objects.all()
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='chat_media', blank=True, null=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver}: {self.message}'
    
