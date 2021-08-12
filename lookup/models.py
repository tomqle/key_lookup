from django.db import models

# Create your models here.

class Key(models.Model):
    name = models.CharField(max_length=255)

class VehicleApplication(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE, blank=True, null=True)
    vehicle_range = models.CharField(max_length=255)
