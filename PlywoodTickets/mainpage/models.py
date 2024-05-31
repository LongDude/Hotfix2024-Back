from django.db import models

# Create your models here.
class Flights(models.Model):
    id_flights=models.BigIntegerField(primary_key=True)
    id_plane=models.BigIntegerField()
    country_plan=models.TextField()
    to_city=models.TextField()
    from_city=models.TextField()
    start=models.TimeField()
    end=models.TimeField()
    price=models.DecimalField(decimal_places=16,max_digits=32)
    