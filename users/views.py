from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import RegisterForm
from users.forms import LoginForm
from django.contrib.auth import login, logout


# Create your views here.
def sign_up(request):
    if request.method =="GET":
         form=RegisterForm()
         
    if request.method=="POST":
        form=RegisterForm(request.POST)
        
        if form.is_valid():
            
            form.save()
        else:
            print("form is not valid ")
    else:
        form=RegisterForm()      
    return render(request,'registration/register.html',{"form":form})


def sign_in(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    return render(request,'registration/login.html',{"form":form})
            
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("sign_in")