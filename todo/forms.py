from django import forms
from .models import TodoModel
class Todoform(forms.ModelForm):
    class Meta:
        model=TodoModel
        fields=['title','status','due_date','user','priority']