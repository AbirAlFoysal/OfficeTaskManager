from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('projects/', views.projectCollection, name='projects'),
    path('projects/<int:project_id>/', views.projectDetail, name='projectDetail'),
    path('testpage/', views.testpage, name='testpage'),
    path('projects/<int:project_id>/addTask/', views.add_task, name='addTask'),
    path('tasks/<int:task_id>/add_subtask/', views.add_subtask, name='add_subtask'),

]