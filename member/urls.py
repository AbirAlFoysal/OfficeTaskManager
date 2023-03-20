from django.urls import path, include, re_path
from . import views

urlpatterns = [
#     path('', home, name='users-home'),
    path('', include('social_django.urls', namespace='social')),
    
    path('register/', views.register, name='users-register'),
    ]