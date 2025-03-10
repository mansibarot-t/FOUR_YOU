from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import UserSerializer, CartSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User  = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Return the currently authenticated user
    
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'message': 'Login successful', 'user_id': user.id}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class CartView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        return Cart.objects.get(user=self.request.user)

    def get(self, request):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    def put(self, request):
        cart = self.get_object()
        serializer = self.get_serializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)