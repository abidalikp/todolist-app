from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Todolist
from .forms import TodoListForm

@login_required
def index(request):
    todo_items = Todolist.objects.filter(user=request.user).order_by('id')
    form = TodoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context)

@login_required
@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.user = request.user
        new_todo.save()

    return redirect('index')

@login_required
def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

@login_required
def deleteTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')

@login_required
def deleteCompleted(request):
    Todolist.objects.filter(completed=True, user=request.user).delete()
    return redirect('index')

@login_required
def deleteAll(request):
    Todolist.objects.filter(user=request.user).delete()
    return redirect('index')
    