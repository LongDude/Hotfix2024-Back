from django.urls import path
from django.urls import include
from personalLocker.views import *
from rest_framework_simplejwt.views import TokenBlacklistView
from . import views

urlpatterns = [
    path('login/',LoginApiView.as_view()),
    path('logout/',LogoutApiView.as_view()),
    path('user/',TokenUser.as_view()),
    path('', views.index, name='index'),
    path('register/',UserRegister.as_view()),
    path('change-profile/',UpdateApiView.as_view())
]