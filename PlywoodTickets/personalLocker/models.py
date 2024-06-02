from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    firstname = models.TextField()
    surname = models.TextField()
    patronymic = models.TextField(null=True)
    phonenumber = models.TextField()
    gender = models.BooleanField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserHistory(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    path = models.TextField()
    title = models.TextField()

    def __str__(self):
        return self.path + self.title