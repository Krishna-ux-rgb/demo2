from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm 
from .models import User

def index(request):
    return render(request , 'users/index.html' , {'title' : 'Index'})

def register(request):
    if request.method == 'POST':
        userForm = UserRegisterForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            username = userForm.cleaned_data['username']
            email = userForm.cleaned_data['email']
            phone_no = userForm.cleaned_data['phone_no']
            password1 = userForm.cleaned_data['password1']
            print(username, email , phone_no , password1)
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request , 'users/register.html' , {'form' : form})

def login(request):
    if request.method == 'POST':
        pass
    else:
        af = AuthenticationForm()
        return render(request, 'users/login.html' , {'form' : af})

