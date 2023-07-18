from django.db import models

class Flight(models.Model):
    flight_from = models.CharField(null=False, max_length=100)
    flight_to = models.CharField(null=False, max_length=100)
    airline = models.CharField(null=False, max_length=200)
    tickets = models.IntegerField(default=0)
    date = models.DateTimeField(null=False)
    image = models.ImageField(upload_to='plane_image', default='plane_image/airplane-flight.webp')

    def __str__(self):
        return self.flight_from + ' --> ' + self.flight_to
