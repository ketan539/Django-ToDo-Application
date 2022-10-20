from django import forms
from .models import task

class taskform(forms.ModelForm):
    class Meta:
        model=task
        fields='__all__'
        widgets={
            'task':forms.TextInput(attrs={'placeholder':'Enter your Task here','class':'c1'})
        }

        labels={
            'task':''
            }