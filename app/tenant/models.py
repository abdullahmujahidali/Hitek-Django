from django.db import models

# Create your models here.


# Backend Apps
from core.abstract_models import ID, Dates


class Tenant(Dates, ID):

    name = models.CharField(max_length=255)
    address = models.TextField()
    region = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    poc = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=11)
