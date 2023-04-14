from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime
from django.utils import timezone
from django.db.models import Q

from django.http import JsonResponse

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
    alltasks = Task.objects.all().filter(related_project = project_id).order_by('deadline')
    expired_tasks = alltasks.filter(status = 2)
    completed_tasks = alltasks.filter(status = 1) 
    task = alltasks.filter(Q(status=0) | Q(status=3))

    links = Link.objects.all().filter(project=project).order_by('-created')
    media = Media.objects.all().filter(project=project).order_by('-created')

 
    for obj in expired_tasks:
        obj.theme = "dark"
        obj.remaining_time = '0D:0H:0M'
        subtasks = Subtask.objects.filter(task = obj)
        obj.subtasks = subtasks
    
    for obj in completed_tasks:
        obj.remaining_time = "Completed"
        subtasks = Subtask.objects.filter(task = obj)
        obj.subtasks = subtasks
        
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
             # set the task status to 2 (completed) if remaining_days is less than 0
            obj.status = 2
            obj.save()
        # remaining time shown below the task 
        obj.remaining_time = f'{remaining_days}D:{remaining_hour}H:{remaining_minutes}M'
        # subtask of respective task from the forloop
        subtasks = Subtask.objects.filter(task = obj)
        # subtask object identification 
        obj.subtasks = subtasks
    # task count 
    total_task = alltasks.count()
    task_completed = completed_tasks.count()
    task_remaining = task.count()
    task_expired = expired_tasks.count()
    # declear forms 
    message_form = MessageForm(prefix = "msg")
    link_Form = LinkForm(request.POST, prefix="link")
    media_Form = MediaForm(request.POST, prefix="media")

    for obj in alltasks:
        obj.comment = TaskComment.objects.filter(task = obj)
        obj.subtask = Subtask.objects.filter(task = obj)
    allsubtasks = Subtask.objects.all().filter(task__related_project = project_id)
    for obj in allsubtasks:
        obj.comment = SubtaskComment.objects.filter(subtask = obj)

    # post methodes of the page 
    if request.method == 'POST':
        # for messages 
        if 'messagebtn' in request.POST:
            msgForm = MessageForm(request.POST, prefix="msg")
            if msgForm.is_valid():
                message = msgForm.save(commit=False)
                message.project = project
                message.sender = request.user
                message.save()
            else:
                message.error(request, 'Message not sent!')

        elif 'linkbtn' in request.POST:
            link_form = LinkForm(request.POST, prefix="link")
            if link_form.is_valid():
                link = link_form.save(commit=False)
                link.project = project
                link.sender = request.user
                link.save()
            else:
                print(link_form.errors)

            # does not work 
        elif 'mediabtn' in request.POST:
            media_form = MediaForm(request.POST, prefix="media")
            if media_form.is_valid():
                media = media_form.save(commit=False)
                media.project = project
                media.sender = request.user
                media.save()
            else:
                print(media_form.errors)

        # for subtasks
        if 'subtask_id' in request.POST and 'status' in request.POST:
            subtask_id = request.POST['subtask_id']
            status = request.POST['status']
            subtask = Subtask.objects.get(pk=subtask_id)
            subtask.status = status
            subtask.save()
            return JsonResponse({'success': True})
        
        # for task status
        if 'task_id' in request.POST and 'status' in request.POST:
            task_id = request.POST['task_id']
            status = request.POST['status']
            task = Task.objects.get(pk=task_id)
            task.status = status
            task.save()
            return JsonResponse({'success': True})
            
        

    # comment = Comment.objects.all().filter(project = project_id)
    # for obj in comment:
    context = {'project': project,'task': task, 'task_completed': task_completed, 'task_remaining': task_remaining, 'total_task': total_task, 'msg': msg,'message_form': message_form, 'expired_tasks': expired_tasks, 'completed_tasks': completed_tasks, 'task_expired': task_expired, 'link_form':link_Form, 'links': links, 'media': media, 'media_form': media_Form, 'alltasks': alltasks, 'allsubtasks': allsubtasks
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




def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    subtasks = Subtask.objects.all().filter(task = task)
    form = TaskForm(request.POST, instance=task)
    if request.method == 'POST':
        if 'subtaskbtn' in request.POST:
            subtask_ids = request.POST.getlist('subtasks')
            for subtask_id in subtask_ids:
                subtask = get_object_or_404(Subtask, pk=subtask_id)
                subtask.delete()

        if 'taskbtn' in request.POST:
            if form.is_valid():
                task = form.save(commit=False)
                task.related_project = task.related_project
                task.save()
                messages.success(request, 'Task updated successfully!')
                return redirect('update_task', task_id=task.id) 
            
        if 'deletetaskbtn' in request.POST:
            task.delete()
            messages.success(request, 'Task deleted successfully!')
            return redirect('projectDetail', project_id=task.related_project.id)
    
    context = {'task': task, 'subtasks': subtasks, 'form': form}
    return render(request, 'TaskManager/update_task.html', context)
 