from django import forms
from task.models import TaskModel
from category.models import CategoryModel

class TaskForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=CategoryModel.objects.all(),
        required=False 
    )
    
    class Meta:
        model = TaskModel
        exclude = ['assign_date']
