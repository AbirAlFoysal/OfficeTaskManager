from django.shortcuts import render
from .models import Chat

# Create your views here.

def allChat(request):
    chats = Chat.objects.all().filter(sender=request.user.id) and Chat.objects.all().filter(receiver=request.user.id).order_by('-created')
    return render(request, 'chat/allChat.html', {'chats':chats})