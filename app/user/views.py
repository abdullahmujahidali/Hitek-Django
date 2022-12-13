from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from user.models import User
from user.serializer import UserSerializer

from core.mixins import PublicViewMixin

from rest_framework import generics

from user.models import User

from rest_framework.permissions import AllowAny

# Create your views here.


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def create(self, request):
        pass

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AccountCreate(PublicViewMixin, generics.ListCreateAPIView):

    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print('data: ', serializer.validated_data)  
            print('asdsad: ', serializer.data)
            return Response(serializer.data)
        else:
            return Response(
                'obj not found'
            )


