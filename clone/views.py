from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')




