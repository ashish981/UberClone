from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
import tkinter
from tkinter import messagebox

import requests
# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                 root = tkinter.Tk()
                 root.withdraw()

            # Message Box
                 messagebox.showinfo("Error", "Username taken")
                 return redirect('register') 
            elif User.objects.filter(email=email).exists():
                 root = tkinter.Tk()
                 root.withdraw()

            # Message Box
                 messagebox.showinfo("Error", "Email taken)")
                 return redirect('register') 
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email = email )
                user.save();
                print('User Created')
                return redirect('login')
        else:
            root = tkinter.Tk()
            root.withdraw()

            # Message Box
            messagebox.showinfo("Error", "Invalid Credentials (Password does not match)")
            return redirect('register')    
        
    else:   
        print('password not matching')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
       
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')    
    else:        
        return render(request, 'login.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

