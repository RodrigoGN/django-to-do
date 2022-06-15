from asyncio import tasks
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Task
from .form import TaskForm
from django.contrib import messages

# Create your views here.
@login_required
def task_list(request):
    search = request.GET.get('search')
    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
        if tasks.count() == 0:
            # if not found, send a message to the user and include button to go back to the list
            messages.info(request, f'Nenhuma tarefa com o nome "{search}" encontrada!', extra_tags='alert alert-warning')
    else:   
        tasks_list = Task.objects.all().order_by('-create_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 6)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks})


@login_required
def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/taskview.html', {'task': task})


@login_required
def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})
    

@login_required    
def edittask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                return render(request, 'tasks/edittask.html', {'form': form , 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form , 'task': task})


@login_required
def deletetask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('/')
