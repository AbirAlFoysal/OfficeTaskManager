from django.db import models

# Create your models here.

class Chat(models.Model):
    message = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='chat_media', blank=True, null=True)

    def __str__(self):
        return self.sender + ' to ' + self.receiver + ' : ' + self.message