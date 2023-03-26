from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('projects/', views.projectCollection, name='projects'),
    path('projects/<int:project_id>/', views.projectDetail, name='projectDetail'),
    path('testpage/', views.testpage, name='testpage'),
]