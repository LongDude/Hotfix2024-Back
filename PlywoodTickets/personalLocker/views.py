from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.views import generic
from django.contrib.auth import authenticate, login
class LoginApiView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user.id)
        return Response({"res1": True})
    
    def post(self,request,*args,**kwargs):
        username = request.data["login"]
        password = request.data["password"]
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            customUser = CustomUserSerializer(user)
            print(customUser.data)
            return Response(customUser.data)
        else:
            return Response(None)
        
class UserApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
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
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})