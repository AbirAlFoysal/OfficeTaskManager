from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    representative = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members')
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    transparent = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    credits = models.IntegerField(default=0)
    description = models.TextField()
    deadline = models.DateTimeField()
    commentOnCompletion = models.TextField()

    def __str__(self):
        return self.title
    
    
class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    credits = models.IntegerField(default=0)
    description = models.TextField()
    dateline = models.DateTimeField()
    commentOnCompletion = models.TextField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask = models.ForeignKey(Subtask, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply
    

class Link(models.Model):
    assigner = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    serial = models.CharField(max_length=5, default='LS1')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link


class Media(models.Model):
    assigner = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    media = models.FileField(upload_to='media/')
    description = models.TextField()
    serial = models.CharField(max_length=5, default='MS1')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.media
    