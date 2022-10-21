
from asyncio.windows_events import NULL
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ContacForm
from .models import Contact

# Create your views here.
def index(request, letter= NULL):
   if letter !=NULL: 
      contac = Contact.objects.filter(name__istartswith=letter)
   else:
      contac = Contact.objects.filter(name__contains=request.GET.get('search', ''))
   context = {
       'contac' : contac 
    }
   return render(request, 'contac/index.html', context)
   
def view(request, id):
   contact = Contact.objects.get(id=id)
   return render(request, 'contac/details.html', {'contact': contact})

def edit(request, id):
   contact = Contact.objects.get(id=id)
   if request.method == 'GET':
      
      form = ContacForm(instance=contact)
      context = {
         'form': form,
         'id': id
      }
      return render(request, 'contac/edit.html', context)

   if request.method == 'POST':
      form = ContacForm(request.POST, instance=contact)
      if form.is_valid():
         form.save()
      context = {
         'form': form,
         'id': id
      }
      messages.success(request, 'Contacto actualizado con exito')
    
      return render(request, 'contac/edit.html', context)

def create(request):
   if request.method == "GET":
      form = ContacForm()
      context = {
      'form': form
      }
      return render(request, 'contac/create.html', context)


   if request.method == 'POST':
      form = ContacForm(request.POST)
      if form.is_valid():
         form.save()
      return redirect('contac')

def delete(request, id):
   contact = Contact.objects.get(id=id)
   contact.delete()
   return redirect('contac')
      
       
  