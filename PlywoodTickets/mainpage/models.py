from django.db import models
from django.urls import reverse
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
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id_flights)])