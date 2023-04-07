from django import forms
from .models import Task, Subtask
from ckeditor.fields import CKEditorWidget

class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['status','created','commentOnCompletion']



class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ('title', 'credits', 'description', 'dateline')

class task_subtask(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__' 
        widgets = {
            'subtasks': forms.CheckboxSelectMultiple(),
        }
