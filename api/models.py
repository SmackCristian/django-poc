from django.db import models


# Create your models here.
class Case(models.Model):
    city_name = models.CharField(max_length=255)
    confirmed = models.IntegerField()
    dead = models.IntegerField()
    recovered = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.city_name
