from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, authenticate
from rest_framework_simplejwt.tokens import AccessToken

from django.shortcuts import render
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .serializers import *
from .models import *
import json
import requests
city=['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai']
class Cities(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    @csrf_exempt
    def get(self,request,*args,**kwargs):
        return Response(city)
class FlightsHistory(APIView):
    permission_classes = [permissions.AllowAny]
    @csrf_exempt
    def get(self,request,*args,**kwargs):
        From=request.GET["from"]
        To=request.GET["to"]
        Date=request.GET["date"]
        Class=request.GET["class"]
        if Class=="Эконом":
            Class=1
        else:
            Class=0
        city.sort()
        print(request.data)
        if request.user.is_authenticated:
            print(request.user.id)
            UserHistory.objects.create(user_id=CustomUser.objects.get(pk=request.user.id),path=request.GET["path"],title=request.GET["title"]).save()
        # user = CustomUser.objects.get(pk=request.user.id)
        # history=UserHistory()
        response=requests.get("http://127.0.0.1:9000/calculate",params={"f":city.index(From),"t":city.index(To),"d":int(Date),"e":int(Class)})
        json_data = json.loads(json.loads(response.text))
        print(json_data)
        return JsonResponse(json_data,safe=False)

class UserRequest(APIView):
    ''' TODO: '''
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get(self, request, *args, **kwargs):

        models = UserHistory.objects.filter(user_id = request.user.id).values('path', 'title')
        print(list(models))
        # paginator = Paginator(models, request.GET.get('page'))
        paginator = Paginator(models, 10)
        pageNumber = request.GET.get('page')

        try:
            paginatedPage = paginator.page(pageNumber)
        except PageNotAnInteger:
            pageNumber = 1
        except EmptyPage:
            pageNumber = paginator.num_pages
        models = paginator.page(pageNumber)
        print(list(models))
        return JsonResponse(list(models), safe=False)
        # user = CustomUser.objects.get(pk=request.user.id)
        # custom_user = CustomUserSerializer(user)

        # histories=UserHistory.objects.filter(user_id=request.user.id)

        # return JsonResponse(list(histories.values("path", "title")), safe=False)

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
        print(request.data)
        if user.check_password(request.data["password"]):
            user.set_password(request.data["newPassword"])

        customUserData = {
            'email':request.data['login'],
            'firstname':request.data['firstName'],
            'surname':request.data['lastName'],
            'phonenumber':request.data['phone'],
            'gender': request.data['gender'],
            'password':user.password
        }
        

        customUser = CustomUserSerializer(user,data=customUserData)

        if customUser.is_valid():
            customUser.save()
            return Response(customUser.data,status = status.HTTP_200_OK)

        return Response(None,status=status.HTTP_200_OK)


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