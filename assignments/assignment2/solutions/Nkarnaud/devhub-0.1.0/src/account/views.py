from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'registration/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()   
    return render(request, 'registration/register.html', {'form': form})