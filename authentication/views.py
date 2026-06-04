from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def loginpage(request):
    context={}

    if request.method=='POST':

        print(request.POST)

        user=authenticate(username = request.POST['username'],password=request.POST['password'])
        print(user)

        if user is not None:
             login(request, user)
             return redirect('/orders/all/customers/')
        else:
            context={
                'error': "*invalid creditlines"
            }        
            
    return render(request,'login.html',context)

def logoutpage(request):
    logout(request)
    return redirect('/')

def singup(request):
    context={}
    if request.method=='POST':

        user_check=user.objects.filter(username=request.POST['username'])
        if (len(user_check)==0):
            new_user=user(username=request.POST['username'],first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],email=request.POST['email'],age=request.POST['age'])
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('/')
        else:
            context={
                'error':"The Username has already exists!"
            }
            return render(request,'singup.html',context)
    return render(request,'singup.html',context)
