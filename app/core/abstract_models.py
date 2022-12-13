# Standard Library
from uuid import uuid4

# Django
from django.db import models

# Backend Apps
from core.validations import order_validation


class Dates(models.Model):
    """A base class for date and time that keeps the time of creation and \
        modification for objects of classes that inherit it."""

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ID(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True


class Ordering(models.Model):
    """An abstract model class that is used where the order of \
        objects is important."""

    order = models.PositiveIntegerField(validators=[order_validation])

    class Meta:
        abstract = True


class Name(models.Model):
    """A class that stores the name for the classes that inherit it."""

    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class UserAwareModel(models.Model):
    """This abstract model adds a foreign key to the inheritee model."""

    user = models.ForeignKey(
        to="user.User", on_delete=models.CASCADE,
        related_name="%(class)s", null=True)

    class Meta:
        abstract = True
