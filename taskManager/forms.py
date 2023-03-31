from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'ckeditor'}))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['status','created','commentOnCompletion']