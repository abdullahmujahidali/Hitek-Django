# DRF
from rest_framework import serializers
from user.models import User

from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    """This serializer is used wherever we need to validate/input \
        a UUID which is optional."""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
