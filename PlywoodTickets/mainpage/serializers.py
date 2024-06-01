from rest_framework import serializers
from .models import Flights

class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flights
        fields=['id_plane','country_plan','to_city','from_city', 'start', 'end', 'price']