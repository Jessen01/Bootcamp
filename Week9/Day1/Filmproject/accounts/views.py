from django.shortcuts import render,redirect
from django import forms 
from .models import *

# Create your views here.
def Signup(request):
    if request.user.is_authenticated:
        return redirect('/films/homepage')
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        
        if password != confirm_password:
            
            return redirect('/accounts/signup/')
        
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')  
    return render(request, "signup.html")

def Login(request):
    if request.user.is_authenticated:
        return redirect('/films/homepage')
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/accounts/signup/")
        else:
            return render(request, "login.html") 
    return render(request, "login.html")

def Logout(request):
    return redirect('/accounts/login/')


def Profile(request,id):
    
    user=user.objects.get(id=id)
    return render(request,user)

















