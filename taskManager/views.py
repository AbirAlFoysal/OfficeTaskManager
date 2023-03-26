from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime
from django.utils import timezone

# Create your views here.

@login_required(login_url='/login')
def index(request):
    user = request.user
    projects = user.members.all()
    return render(request, 'taskManager/index.html',{'projects': projects})

def testpage(request):
    return render(request, 'taskManager/testpage.html')

def projectCollection(request):
    ongoing_projects = Project.objects.all().filter(status = 0)
    finished_projects = Project.objects.all().filter(status = 1)
    return render(request, 'taskManager/projectCollection.html',{'ongoing_projects': ongoing_projects, 'finished_projects': finished_projects})

def projectDetail(request, project_id):
    msg =  Message.objects.all().filter(project = project_id)
    project = Project.objects.get(id=project_id)
    task = Task.objects.all().filter(related_project = project_id).order_by('deadline')

    for obj in task:
        deadline = obj.deadline
        remaining_time = deadline - timezone.now()
        remaining_days = remaining_time.days + 1
        remaining_hour = remaining_time.seconds // 3600
        remaining_minutes = (remaining_time.seconds % 3600) // 60
        obj.remaining_time = f'{remaining_days}D:{remaining_hour}H:{remaining_minutes}M'
        if remaining_days <= 3 and remaining_days >= 1:
            theme = "warning"
        elif remaining_days < 1:
            theme = "danger"
        else:
            theme = "success"
        obj.theme = theme

        subtasks = Subtask.objects.filter(task = obj)
        obj.subtasks = subtasks
    # task = task.order_by(-deadline)
    total_task = Task.objects.all().filter(related_project = project_id).count()
    task_completed = Task.objects.all().filter(related_project = project_id, status = 1).count()
    task_remaining = Task.objects.all().filter(related_project = project_id, status = 0).count()

    context = {'project': project, 'task': task, 'task_completed': task_completed, 'task_remaining': task_remaining, 'total_task': total_task, 'msg': msg}
    return render(request, 'taskManager/project.html', context)