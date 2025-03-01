import string
import random

from django.db import models

# Create your models here.

class BaseModel(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Key(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TransponderKey(Key):
    sku = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class KeyShell(BaseModel):
    name = models.CharField(max_length=255)
    key = models.ForeignKey(Key, on_delete=models.PROTECT, blank=True, null=True)
    sku = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Remote(Key):
    sku = models.CharField(max_length=255)
    fcc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class RemoteShell(BaseModel):
    name = models.CharField(max_length=255)
    remote = models.ForeignKey(Remote, on_delete=models.PROTECT, blank=True, null=True)
    sku = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class EmergencyKey(BaseModel):
    name = models.CharField(max_length=255)
    remote = models.ForeignKey(Remote, on_delete=models.PROTECT, blank=True, null=True)
    sku = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class VehicleApplication(BaseModel):
    key = models.ForeignKey(Key, on_delete=models.CASCADE, blank=True, null=True)
    key_shell = models.ForeignKey(KeyShell, on_delete=models.CASCADE, blank=True, null=True)
    remote_shell = models.ForeignKey(RemoteShell, on_delete=models.CASCADE, blank=True, null=True)
    emergency_key = models.ForeignKey(EmergencyKey, on_delete=models.CASCADE, blank=True, null=True)
    vehicle_range = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle_range

class Distributor(BaseModel):
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

class DistributorKey(BaseModel):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'key')

class DistributorTransponderKey(BaseModel):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    transponder_key = models.ForeignKey(TransponderKey, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'transponder_key')

class DistributorRemote(BaseModel):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    remote = models.ForeignKey(Remote, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    def __str__(self):
        return f"{ self.distributor.name } [{ self.link }]"

    class Meta:
        unique_together = ('distributor', 'remote')

class DistributorKeyShell(BaseModel):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    key_shell = models.ForeignKey(KeyShell, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'key_shell')

class DistributorRemoteShell(BaseModel):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    remote_shell = models.ForeignKey(RemoteShell, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'remote_shell')

class DistributorEmergencyKey(BaseModel):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    emergency_key = models.ForeignKey(EmergencyKey, on_delete=models.CASCADE)
    link = models.URLField(max_length=1024, blank=True)

    class Meta:
        unique_together = ('distributor', 'emergency_key')