from django.contrib import admin
from lookup.models import Key, VehicleApplication

# Register your models here.

class VehicleApplicationInLine(admin.TabularInline):
    model = VehicleApplication

@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]
