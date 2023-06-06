from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# from django.conf import settings
# User = settings.AUTH_USER_MODEL

 
# Create your models here.

class Project(models.Model):
    representative = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members')
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    description = RichTextField(default='No description provided', blank=False, null=False)
    deadline = models.DateTimeField()
    transparent = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    related_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = RichTextField(blank=False, null=False)
    status = models.IntegerField(default=0) # 0:not started, 1: completed, 2: expired, 3:ongoing
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    credits = models.IntegerField(default=0)
    description = RichTextField(default='No description provided')
    deadline = models.DateTimeField()
    commentOnCompletion = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    
class Subtask(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    related_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    credits = models.IntegerField(default=0)
    description = RichTextField(default='No description provided', blank=True, null=True)
    deadline = models.DateTimeField()
    commentOnCompletion = RichTextField(default='No comments', blank=True, null=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    body = RichTextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body

class TaskComment(models.Model):
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment = RichTextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
class SubtaskComment(models.Model):
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subtask = models.ForeignKey(Subtask, on_delete=models.CASCADE)
    comment = RichTextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    
# class Reply(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     critic = models.ForeignKey(User, on_delete=models.CASCADE)
#     reply = RichTextField(blank=False, null=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.reply
    

class Link(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = RichTextField(default='No description provided', blank=True, null=True)
    link = models.URLField()
    serial = models.CharField(max_length=5, default='LS1')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link


class Media(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    media = models.FileField(upload_to='media/')
    description = RichTextField(default='No description provided', blank=True, null=True)
    serial = models.CharField(max_length=5, default='MS1')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.media
    