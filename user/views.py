from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.models import Token 
from rest_framework_simplejwt.authentication import JWTAuthentication
# from .auth import LoginView

class Userapi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

