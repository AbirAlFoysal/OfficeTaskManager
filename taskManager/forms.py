from django import forms
from .models import Task, Subtask, Message
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


class DeleteTaskForm(forms.Form):
    confirm_delete = forms.BooleanField(required=True)
