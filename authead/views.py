from django.shortcuts import render
from .serializers import EmailRegistrationSerializer, User
from rest_framework import generics, serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializers = EmailRegistrationSerializer

