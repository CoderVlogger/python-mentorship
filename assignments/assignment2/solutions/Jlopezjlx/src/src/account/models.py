from django.contrib.auth.models import AbstractUser
from django.db import models





class Account(AbstractUser):
    """
    With this class we are customazing Django's User model.
    More information here:
    https://docs.djangoproject.com/en/dev/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """
    REQUIRED_FIELDS = ['email']
