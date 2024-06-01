from django.shortcuts import render
from django.views import generic
from .models import Flights
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
# Create your views here.
class Tickets(generic.ListView):
    model=Flights
class TicketsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @csrf_exempt
    def get(self,request,*args,**kwargs):
        print(request.data)
        return Response([1,2,3])
def main(request):
    return render(request,'main.html')