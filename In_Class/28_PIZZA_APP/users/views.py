from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .form import UserForm 
# Create your views here.
from django.contrib.auth import login,logout

def register(request):
    # form = UserCreationForm()  #! kendi formumu olusturmadan önce bunu kullanmistim.
    form = UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={
        'form' : form
    }
    return render(request, "users/register.html", context)

#! Djangonun user icin default olusturdugu formu kullaniyoruz. in 6.line...



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Do not forget to provide the user to the login function
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')