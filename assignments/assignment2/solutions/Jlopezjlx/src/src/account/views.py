from .forms import CustomCreateUser
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse 






def index(request):
   return render(request, "account/index.html")


def register(request):
   if request.method == 'POST':
      form = CustomCreateUser(request.POST)
      if form.is_valid():
         User = form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         User = authenticate(username=username, password=raw_password)
         auth_login(request, User)
         return HttpResponseRedirect(reverse("index"))
   else:  
      form = CustomCreateUser()    
   return render(request, "account/register/register.html", {'form': form})


def login(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('psw')
      user = authenticate(username=username, password=password)
      if user:
         if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
         else: 
            return HttpResponse ("Your account was inactive")   
      else: 
         print("Someone tried to log in and Failed")
         return HttpResponse ("Invalid credentials")
   else:
      return render(request, "account/login/login.html")

