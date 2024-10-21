import string
import random

from django.db import models

# Create your models here.

class Key(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TransponderKey(Key):
    sku = models.CharField(max_length=255)

    def __str__(self):
        return '(id: ' + str(self.id) + ') ' + self.name

class KeyShell(models.Model):
    name = models.CharField(max_length=255)
    key = models.ForeignKey(Key, on_delete=models.PROTECT, blank=True, null=True)
    sku = models.CharField(max_length=255)

    def __str__(self):
        return '(id: ' + str(self.id) + ') ' + self.name

class Remote(Key):
    sku = models.CharField(max_length=255)
    fcc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '(id: ' + str(self.id) + ') ' + self.name

class RemoteShell(models.Model):
    name = models.CharField(max_length=255)
    remote = models.ForeignKey(Remote, on_delete=models.PROTECT, blank=True, null=True)
    sku = models.CharField(max_length=255)

    def __str__(self):
        return '(id: ' + str(self.id) + ') ' + self.name

class EmergencyKey(models.Model):
    name = models.CharField(max_length=255)
    remote = models.ForeignKey(Remote, on_delete=models.PROTECT, blank=True, null=True)
    sku = models.CharField(max_length=255)

    def __str__(self):
        return '(id: ' + str(self.id) + ') ' + self.name

class VehicleApplication(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE, blank=True, null=True)
    key_shell = models.ForeignKey(KeyShell, on_delete=models.CASCADE, blank=True, null=True)
    remote_shell = models.ForeignKey(RemoteShell, on_delete=models.CASCADE, blank=True, null=True)
    emergency_key = models.ForeignKey(EmergencyKey, on_delete=models.CASCADE, blank=True, null=True)
    vehicle_range = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle_range

class Distributor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=16, blank=True, null=True, unique=True, editable=False)
    logo = models.ImageField(upload_to='distributor_logos/', blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                self.code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

                print('hi')

                if not Distributor.objects.filter(code=self.code):
                    break

        return super(Distributor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class DistributorKey(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'key')

class DistributorTransponderKey(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    transponder_key = models.ForeignKey(TransponderKey, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'transponder_key')

class DistributorRemote(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    remote = models.ForeignKey(Remote, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'remote')

class DistributorKeyShell(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    key_shell = models.ForeignKey(KeyShell, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'key_shell')

class DistributorRemoteShell(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    remote_shell = models.ForeignKey(RemoteShell, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'remote_shell')

class DistributorEmergencyKey(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    emergency_key = models.ForeignKey(EmergencyKey, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'emergency_key')