# Django
# Django
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# 3rd Party Libraries
from user.manager import CustomBaseUserManager

# Backend Apps
from core.abstract_models import ID, Dates


class User(AbstractBaseUser, Dates, ID):

    is_owner = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'

    objects = CustomBaseUserManager()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "user"
