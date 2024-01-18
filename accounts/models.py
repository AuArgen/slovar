from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Add related_name to resolve the clash
        related_query_name="user",
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_set",  # Add related_name to resolve the clash
        related_query_name="user",
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.username