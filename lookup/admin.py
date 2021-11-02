from django.contrib import admin
from lookup.models import Key, Remote, VehicleApplication

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
