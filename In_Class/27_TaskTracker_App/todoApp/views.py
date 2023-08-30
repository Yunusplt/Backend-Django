from django.shortcuts import render
from .models import Todo
# Create your views here.

#! FBV #####################
def todo_list(request):
    todos = Todo.objects.all()
    context={
        "todos" : todos
    }
    return render(request,'todoApp/list.html',context)
    # return render(request,html,context)

from .forms import TodoForm
from django.shortcuts import redirect

def todo_add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    context={
        'form' : form
    }
    return render(request,'todoApp/add.html', context )
    # return render(request,html,context)


def todo_update(request,pk):
    todo=Todo.objects.get(id=pk)    #!istenilen obje elde et
    form = TodoForm(instance=todo)  #! formu elde ettigim tek bir obje ile olusturacak.
    if request.method=="POST":      #!formu tekrar olustur güncellenmis veriler ile
        form=TodoForm(request.POST, instance=todo)   #!yeniden kayit olusturmamasi icin instance todo
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    context={
        'form' : form,
        "todo" : todo
    }
    return render(request,'todoApp/update.html', context )


def todo_delete(request,pk):
    todo=Todo.objects.get(id=pk)  
    todo.delete() 
    return redirect('todo_list')
    
#!--------------------------------

#! CBV #########################
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
) 
class TodoListView(ListView):
    model = Todo
    #!eger farkli isimde bir html(template) kullanacaksaniz 
    # template_name="todoApp/list.html"
from django.urls import reverse_lazy
class TodoCreateView(CreateView):
    model=Todo
    form_class=TodoForm
    success_url = reverse_lazy('todo_list')
class TodoUpdateView(UpdateView):
    model=Todo
    form_class=TodoForm
    success_url = reverse_lazy('todo_list')
class TodoDeleteView(DeleteView):
    model=Todo
    success_url = reverse_lazy('todo_list')

