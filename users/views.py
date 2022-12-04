from django.contrib.auth import login, get_user_model, authenticate, logout
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import fields
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView


class SignupSerializer(Serializer):
    email = fields.EmailField()
    password = fields.CharField(max_length=255)


class SignupView(APIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if get_user_model().objects.filter(email=serializer.data['email']).exists():
            raise ValidationError('존재하는이메일')
        user = get_user_model().objects.create_user(**serializer.data)
        return Response({'email': user.email})


class SigninSerializer(Serializer):
    email = fields.EmailField()
    password = fields.CharField(max_length=255)


class SigninView(APIView):
    serializer_class = SigninSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.data)
        if not user:
            raise ValidationError
        login(request, user)
        return Response({'email': user.email})


class SignoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response(status=204)
