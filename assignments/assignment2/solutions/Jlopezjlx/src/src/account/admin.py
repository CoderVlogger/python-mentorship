from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account import models as account_models
from .forms import CustomCreateUser


class CustomUser(UserAdmin):
    add_form = CustomCreateUser
    model = account_models.Account
    list_display = ['username', 'password', 'email']


admin.site.register(account_models.Account, UserAdmin)
