from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from account.models import Account


class AccountCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = Account
        fields = ('username','first_name', 'last_name' ,'email', 'password1', 'password2')

class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = UserChangeForm.Meta.fields