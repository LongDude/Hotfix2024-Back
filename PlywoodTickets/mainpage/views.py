from django.shortcuts import render
from django.views import generic
from .models import Flights
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
# Create your views here.
def main(request):
    return render(request,'main.html')