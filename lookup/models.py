from django.db import models

# Create your models here.

class Key(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Remote(Key):
    sku = models.CharField(max_length=255)
    fcc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class VehicleApplication(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE, blank=True, null=True)
    vehicle_range = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle_range
