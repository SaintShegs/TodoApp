from django import forms
from .models import *
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'




class TodoForm(forms.ModelForm):
    class Meta:
        model= Todo
        fields= ('name','details', 'due_date','completed')



        labels={
            'name':"Task Name",
            'details':"Details",
            'due_date':"Due Date",
            'completed':"Completed"
        }


        widgets={
            'name': forms.TextInput(),
            'details':forms.Textarea(),
            'due_date':DateInput(),
            'completed':forms.CheckboxInput()
        }
        

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}


