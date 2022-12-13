# DRF
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """This serializer is used wherever we need to validate/input \
        a UUID which is optional."""

    id = serializers.UUIDField(required=False)
    pass
