# Django
# Django
from django.contrib.auth.models import AbstractUser
from django.db import models

# 3rd Party Libraries
from user.manager import CustomBaseUserManager

# Backend Apps
from core.abstract_models import ID, Dates


class User(AbstractUser, Dates, ID):

    is_owner = models.BooleanField(default=False)

    objects = CustomBaseUserManager()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "user"
