from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('register/',views.register,name="register")
]