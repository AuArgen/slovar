# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Добавьте дополнительные поля, если необходимо
    pass
