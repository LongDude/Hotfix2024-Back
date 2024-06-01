from django.urls import path
from django.urls import include
from personalLocker.views import UserApiView,LoginApiView,LogoutApiView
from . import views

urlpatterns = [
    path('login/',LoginApiView.as_view()),
    path('logout/',LogoutApiView.as_view()),
    path('', views.index, name='index'),
    path('register/',views.register,name="register"),
    path('',UserApiView.as_view(),name="update")
]