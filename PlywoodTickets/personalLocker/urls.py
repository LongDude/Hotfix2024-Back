from django.urls import path
from django.urls import include
from personalLocker.views import *

urlpatterns = [
    path('login/',LoginApiView.as_view()),
    path('logout/',LogoutApiView.as_view()),
    path('user/',TokenUser.as_view()),
    path('register/',UserRegister.as_view()),
    path('change-profile/',UpdateApiView.as_view()),
    path('requests/',UserRequest.as_view()),
    path('flights/',FlightsHistory.as_view())
]