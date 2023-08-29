from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>welcome to django template</h1>')
def home(request):
     context={         
          }             
     return render(request,'templateApp/home.html',context)

def body(request):
     context={
          'title':'clarusway',
          'path':'FS',
          'list':['yunus','ozlem','fatih','esra','huseyin','nihal','emirhan','halit','irfan'],
          'dict':{
               'k1':'value1',
               'k2':'value2'
          },
          'number':0,
          'desc':'this template from APP dir'
          }
         
     
     return render(request,'templateApp/index.html',context)
    # return render(request,'templateApp/index.html',{'name':'yunus'})
from .models import Student

def studentView(request):
     students=Student.objects.all()
     context={ 
          'students':students,
          }             
     return render(request,'templateApp/student.html',context)

from .forms import StudentForm
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy

def student_addView(request):
     form=StudentForm()
     if request.method=="POST":
          form=StudentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/student')
     context={
          'form':form
     }
     return render(request,'templateApp/student_add.html',context)

class StudentAddView(generic.CreateView):
     model=Student
     form_class=StudentForm
     success_url=reverse_lazy('list')  #! urldeki name
     template_name='templateApp/student_add.html'


#! student_form.html istiyor. genericviews. yada ne kullaniyorsan belirtmek icin template_name icinde belirtiyoruz.


class StudentListView(generic.ListView):
     model=Student
     # form_class=StudentForm
     # success_url=reverse_lazy('list')  #! urldeki name
     # template_name='templateApp/student_add.html'


#! burdan asagidaki viewler <int:pk> icerdigi icin css i görmüyor.
class StudentDetailView(generic.DetailView):
     model=Student
     #! default olarak student_detail.html arar----

class StudentUpdateView(generic.UpdateView):
     model=Student
     form_class=StudentForm
     success_url=reverse_lazy('list')  #! urldeki name
     template_name='templateApp/student_add.html'
     #! default olarak student_form.html istiyor add deki gibi