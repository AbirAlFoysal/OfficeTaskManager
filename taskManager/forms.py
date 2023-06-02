from django import forms
from .models import Task, Subtask, Message, Link, Media, Project, SubtaskComment, TaskComment
from ckeditor.fields import CKEditorWidget
from django.forms import widgets

class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['status','created','commentOnCompletion']



class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ('title', 'description', 'deadline', 'credits')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['description', 'link']
 
class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['description', 'media']

class DeleteTaskForm(forms.Form):
    confirm_delete = forms.BooleanField(required=True)



class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ['comment']

class SubtaskCommentForm(forms.ModelForm):
    class Meta:
        model = SubtaskComment
        fields = ['comment']