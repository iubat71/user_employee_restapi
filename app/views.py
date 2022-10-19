from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from .serializer import EmployeeSerializer
from .models import Employees
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Token.objects.create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
          
            "message": "User Created Successfully",
        })
    

class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeApi(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


