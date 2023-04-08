from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime
from django.utils import timezone


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *

# Create your views here.

@login_required(login_url='/login')
def index(request):
    user = request.user
    projects = user.members.all()
    return render(request, 'taskManager/index.html',{'projects': projects})

def testpage(request):
    project = Project.objects.all().filter(id = 1)
    task = Task.objects.all().filter(related_project = 2)
    for obj in task:
        subtasks = Subtask.objects.filter(task = obj)
        obj.subtasks = subtasks
    if request.method == 'POST':
        object_type = request.POST.get('object_type')

        if object_type == 'task':
            # handle task submission
            pass
        elif object_type == 'subtask':
            # handle subtask submission
            pass

    # render the template for the page
    

    return render(request, 'taskManager/testpage.html',{'project': project, 'task': task})


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
        # remaining time calculation for each task 
        remaining_time = deadline - timezone.now()
        remaining_days = remaining_time.days + 1
        remaining_hour = remaining_time.seconds // 3600
        remaining_minutes = (remaining_time.seconds % 3600) // 60
        # task theme determination:
            # if 3 days remains, warning 
        if remaining_days <= 3 and remaining_days >= 1:
            theme = "warning"
            # if 1 day remains, danger 
        elif remaining_days < 1:
            theme = "danger"
        else:
            # default success 
            theme = "success"
        obj.theme = theme
            # if day is less than 0, its expired(dark)
        if remaining_days < 0 :
            remaining_days = 0
            remaining_hour = 0
            remaining_minutes = 0
            obj.theme = "dark"
        # remaining time shown below the task 
        obj.remaining_time = f'{remaining_days}D:{remaining_hour}H:{remaining_minutes}M'
        # subtask of respective task from the forloop
        subtasks = Subtask.objects.filter(task = obj)
        # subtask object identification 
        obj.subtasks = subtasks
    # task count 
    total_task = Task.objects.all().filter(related_project = project_id).count()
    task_completed = Task.objects.all().filter(related_project = project_id, status = 1).count()
    task_remaining = Task.objects.all().filter(related_project = project_id, status = 0).count()

    # declear forms 
    message_form = MessageForm(prefix = "msg")

    # post methodes of the page 
    if request.method == 'POST':
        pass
        # for messages 
        if 'messagebtn' in request.POST:
            msgForm = MessageForm(request.POST, prefix = "msg")
            if msgForm.is_valid():
                message = msgForm.save(commit=False)
                message.project = project
                message.sender = request.user
                message.save()
                return redirect('projectDetail', project_id=project_id)
            else:
                messages.error(request, 'Message not sent!')
                msgForm = MessageForm()
                return redirect('projectDetail', project_id=project_id)
        return redirect('projectDetail', project_id=project_id)
        



    # comment = Comment.objects.all().filter(project = project_id)
    # for obj in comment:


    context = {'project': project,
            'task': task, 'task_completed': task_completed, 'task_remaining': task_remaining, 'total_task': total_task, 'msg': msg,
            'message_form': message_form
            
            }
    
    return render(request, 'taskManager/project.html', context)





def add_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(related_project = project)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.related_project = project
            task.save()
            messages.success(request, 'Task added successfully!')
            return redirect('projectDetail', project_id=project_id)
    else:
        form = TaskForm()
    return render(request, 'taskManager/addTask.html', {'form': form, 'project': project, 'tasks': tasks})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task, Subtask
from .forms import SubtaskForm

def add_subtask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    subtasks = Subtask.objects.filter(task = task)
    project = task.related_project
    if request.method == 'POST':
        form = SubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.created_by = request.user
            subtask.related_project = project
            subtask.save()
            messages.success(request, 'Subtask added successfully!')
            return redirect('projectDetail', project_id=project.id)
    else:
        form = SubtaskForm()
    return render(request, 'TaskManager/addSubTask.html', {'form': form, 'task': task, 'subtasks': subtasks, 'project': project})
