from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from account.forms import AccountCreateForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignupView( generic.CreateView):
    form_class = AccountCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'