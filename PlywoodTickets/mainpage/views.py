from django.shortcuts import render
from django.views import generic
from .models import Flights
from rest_framework.views import APIView
# Create your views here.
class Tickets(generic.ListView):
    model=Flights
class TicketsApiView(APIView):
    pass
def main(request):
    return render(request,'main.html')