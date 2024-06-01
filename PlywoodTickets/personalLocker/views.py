from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, authenticate
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.views import generic
from django.contrib.auth import login,logout, get_user
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class LogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        print(request.user)
        logout(request)
        # token = request.headers['Authorization']
        # token=token.replace("Bearer ","")
        # try:
        #     print(token)
        #     ptoken = AccessToken(token)
        #     ptoken.blacklist()
        # except Exception as e:
        #     return Response({'error': 'Jopa'}, status=status.HTTP_400_BAD_REQUEST)
        print(not request.user.is_authenticated)
        return Response(not request.user.is_authenticated)

        print(request.user.auth_token)
        request.user.auth_token.delete()
        return Response(True)

class TokenUser(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @csrf_exempt
    def get(self, request, *args, **keywords):
        user=CustomUser.objects.get(pk=request.user.id)
        cusUser = CustomUserSerializer(user)
        return Response(cusUser.data)

class LoginApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self,request,*args,**kwargs):
        data=request.data
        username = request.data["login"]
        password = request.data["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response(None)


        refresh = AccessToken.for_user(user)
        refresh.payload.update({'user_id': user.id, 'email': user.email})
        return Response({"token":str(refresh)})        

class UserApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        print(request.user.id)
        user=CustomUser.objects.get(pk=request.user.id)
        customUserData = {
            'email': request.data.get("email")
        }
        customUser = CustomUserSerializer(user,data=customUserData)
        if customUser.is_valid():
            customUser.save()
            return Response(customUser.data,status = status.HTTP_200_OK)
        return Response(customUser.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
def index(request):
    ID=request.user.id
    user=CustomUser.objects.get(pk=ID)
    context={'firstname':user.firstname,
            'surname':user.surname,
            'patronymic':user.patronymic,
            'phonenumber':user.phonenumber,
            'email':user.email,
            'gender': user.gender }
    return render(request,'index.html',context=context)
class UserRegister(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        print(request.data)
        user = CustomUserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(True)
        else:
            return Response(None)