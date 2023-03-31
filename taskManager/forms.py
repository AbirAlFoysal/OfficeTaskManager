from django import forms
from .models import Task
from ckeditor.fields import CKEditorWidget

class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['status','created','commentOnCompletion']