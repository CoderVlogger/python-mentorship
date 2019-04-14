from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account import models as account_models


admin.site.register(account_models.Account, UserAdmin)
