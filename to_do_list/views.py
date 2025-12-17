from django.shortcuts import render, redirect
from . models import Todolist
from . forms import Todolistform
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    todo_tasks = Todolist.objects.order_by('id')
    form = Todolistform()
    context = {'todo_tasks' : todo_tasks, 'form':form}
    return render(request, 'todolist.html', context)

@require_POST
def addTodoitem(request):
    form = Todolistform(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text'] # get the submitted text
        Todolist.objects.create(text=text)  # save to the database
    return redirect('todolist')

def completedTodo(request,todo_id):
    todo = Todolist.objects.get(pk = todo_id)
    todo.completed = True
    todo.save()
    return redirect('todolist')

def deletecompleted(request):
    Todolist.objects.filter(completed = True).delete()
    return redirect('todolist')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('todolist')