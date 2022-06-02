from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from django.http import HttpResponse
from .models import *
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm



# Create your views here.
@login_required(login_url='/')
def todo_list(request):
    current_user=request.user
    todos = Todo.objects.filter(user=current_user)
    context={
        "todo_list":todos
    }

    return render(request, "Todoapp/todo_list.html", context)



@login_required(login_url='/')
def todo_pending(request):
    current_user=request.user
    todos=Todo.objects.filter(completed="False" , user=current_user )
    print(todos)
    
    context = {"todo_list" :todos}
    return render(request, "Todoapp/todo_pending.html" , context)




@login_required(login_url='/')
def todo_completed(request):
    current_user=request.user
    todos=Todo.objects.filter(completed="True" , user=current_user)
    print(todos)
    
    context = {"todo_list" :todos}
    return render(request, "Todoapp/todo_completed.html" , context)








# CRUD - Create , Retrieve, Updata, Delete, List
 

@login_required(login_url='/')
def todo_detail(request, id):
    todo= Todo.objects.get(id=id)
    context={
        "todo": todo
    }
    return render(request, "Todoapp/todo_detail.html", context)



@login_required(login_url='/')
def todo_create(request):
    instance=Todo(user=request.user)
    form=TodoForm(request.POST or None , instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/task_lists')
        # or we could also do this
            # print(form.cleaned_data)
            # name=form.cleaned_data['name']
            # due_date=form.cleaned_data['due_date']
            # print(name,due_date)
            # # create a todo object
            # new_todo=Todo.objects.create(name=name, due_date=due_date)
      
    context={
        "form": form
    }
    return render(request, "Todoapp/todo_create.html", context)




@login_required(login_url='/')
def todo_update(request, id):
    todo= Todo.objects.get(id=id)

    form=TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/task_lists')

    context={
        "form": form
    }
    return render(request, "Todoapp/todo_update.html", context)



@login_required(login_url='/')
def todo_delete(request, id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect("/task_lists")
    



class SignupView(generic.CreateView):
    template_name= "registration/signup.html"

    form_class=CustomUserCreationForm

    def get_success_url(self):
        return reverse("todos:Login")


    
