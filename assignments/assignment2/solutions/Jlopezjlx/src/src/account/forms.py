from django.contrib.auth import get_user_model
from .models import Account
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



User = get_user_model()

class CustomCreateUser(UserCreationForm):

    class Meta:
        model = Account
        fields = ('username',)