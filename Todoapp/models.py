from datetime import date
from django.http import request

from django.db import models
from django.contrib.auth import get_user_model,get_user


# Create your models here.

Users= get_user_model()





class Todo(models.Model):
   
    user= models.ForeignKey(Users, null=True, on_delete=models.CASCADE, blank=False)
    name= models.CharField(max_length=30)
    date_created=models.DateField(default=date.today)
    details=models.TextField(max_length=500, default="")
    due_date = models.DateField(default=date.today)
    completed= models.BooleanField()

    def __str__(self):
        return f'{self.name}-----CREATED BY: {self.user}'
    
    





