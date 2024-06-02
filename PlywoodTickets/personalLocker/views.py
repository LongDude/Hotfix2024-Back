from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, authenticate
from rest_framework_simplejwt.tokens import AccessToken

from django.shortcuts import render
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

from .serializers import CustomUserSerializer
from .models import CustomUser
import json


class UserRequest(APIView):
    ''' TODO: '''
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=request.user.id)
        custom_user = CustomUserSerializer(user)
        paths = custom_user.data["path"]
        titles = custom_user.data["title"]
        responce=[]
        if paths!=None and titles!=None:
            for path,title in zip(paths,titles):
                responce.append({"path":path,"title":title})
        return Response(responce)

    def post(self,request,*args,**kwargs):
        user = CustomUser.objects.get(pk=request.user.id)
        custom_user = CustomUserSerializer(user)
        custom_user.data["requests"].append(request.data)
        return Response(True)


class TokenUser(APIView):
    ''' GET: Возвращает пользователя по токену сессии '''
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get(self, request, *args, **keywords):
        user=CustomUser.objects.get(pk=request.user.id)
        custom_user = CustomUserSerializer(user)
        return Response(custom_user.data)


class UpdateApiView(APIView):
    '''PUT: Редактирует данные учётной записи текущего пользователя'''
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def put(self, request, *args, **kwargs):
        user=CustomUser.objects.get(pk=request.user.id)

        if user.check_password(request.data["password"]):
            user.set_password(request.data["newpassword"])

        customUserData = {
            'email':request.data['email'],
            'firstname':request.data['firstname'],
            'surname':request.data['surname'],
            'phonenumber':request.data['phonenumber'],
            'gender': request.data['gender']
        }

        customUser = CustomUserSerializer(user,data=customUserData)

        if customUser.is_valid():
            customUser.save()
            return Response(customUser.data,status = status.HTTP_200_OK)

        return Response(customUser.errors,status=status.HTTP_400_BAD_REQUEST)


class UserRegister(APIView):
    '''POST: Регистрирует нового пользователя'''
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        user = CustomUserSerializer(data=request.data)

        if user.is_valid():
            user.save()
            return Response(True)
        else:
            return Response(None)


class LoginApiView(APIView):
    '''POST: Вход в учётную запись'''
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self,request,*args,**kwargs):
        data = request.data
        username = request.data["login"]
        password = request.data["password"]
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response(None)

        refresh = AccessToken.for_user(user)
        refresh.payload.update({'user_id': user.id, 'email': user.email})
        return Response({"token":str(refresh)})  


class LogoutApiView(APIView):
    '''POST: Выход из учетной записи'''
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(not request.user.is_authenticated)