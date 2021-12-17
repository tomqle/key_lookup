from django.contrib import admin
from lookup.models import Key, Remote, VehicleApplication, Distributor, DistributorKey

# Register your models here.

class VehicleApplicationInLine(admin.TabularInline):
    model = VehicleApplication

@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

@admin.register(Remote)
class RemoteAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

class DistributorKeyInLine(admin.TabularInline):
    model = DistributorKey

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    inlines = [
        DistributorKeyInLine,
    ]

    readonly_fields = ('code', )

