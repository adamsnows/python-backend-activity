from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = UserSerializer
    queryset = User.objects.all()
