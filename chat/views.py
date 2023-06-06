from django.shortcuts import render
from .models import Chat
from django.contrib.auth.models import User	

# Create your views here.

def allChat(request):
    myChats = Chat.objects.all().filter(sender=request.user.id) and Chat.objects.all().filter(receiver=request.user.id).order_by('-created')
    allContacts = User.objects.all().exclude(id=request.user.id)
    return render(request, 'chat/allChat.html', {'myChats': myChats, 'allContacts': allContacts})