from django.urls import path
from django.urls import include
from personalLocker.views import UserApiView
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('register/',views.register,name="register"),
    path('',UserApiView.as_view(),name="update")
]