from django.shortcuts import redirect, render
from django.contrib import messages

from todo.forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
       'todo' : todo 
    }
    return render(request, 'todo/index.html', context)

def todo_view(request, id):
   todo = Todo.objects.get(id=id)
   context = {
    'todo' : todo,
    'id': id
   }
   return render(request, 'todo/details.html', context)
   
def todo_edit(request, id):
   contact = Todo.objects.get(id=id)
   if request.method == 'GET':
      
      form = TodoForm(instance=contact)
      context = {
         'form': form,
         'id': id
      }
      return render(request, 'todo/edit.html', context)

   if request.method == 'POST':
      form = TodoForm(request.POST, instance=contact)
      if form.is_valid():
         form.save()
      context = {
         'form': form,
         'id': id
      }
      messages.success(request, 'Contacto actualizado con exito')
    
      return render(request, 'todo/edit.html', context)


def todo_create(request):
   if request.method == "GET":
      form = TodoForm()
      context = {
      'form': form
      }
      return render(request, 'todo/create.html', context)


   if request.method == 'POST':
      form = TodoForm(request.POST)
      if form.is_valid():
         form.save()
      return redirect('todo')

def todo_delete(request, id):
   contact = Todo.objects.get(id=id)
   contact.delete()
   return redirect('todo')