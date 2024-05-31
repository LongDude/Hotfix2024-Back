from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
]