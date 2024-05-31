from django.shortcuts import render
from django.views import generic
from .models import Flights
# Create your views here.
def main(request):
    return render(request,'main.html')
class tickets(generic.ListView):
    model=Flights