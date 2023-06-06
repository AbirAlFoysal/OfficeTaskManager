from django.urls import path
from . import views

urlpatterns = [
    path('chatlist/', views.allChat, name='chatlist'),
]