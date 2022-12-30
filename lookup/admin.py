from django.contrib import admin
from lookup.models import Key, Remote, VehicleApplication, Distributor, DistributorKey, KeyShell, RemoteShell, EmergencyKey

# Register your models here.

class VehicleApplicationInLine(admin.TabularInline):
    model = VehicleApplication
    fields = ('vehicle_range',)

@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]
    def get_queryset(self, request):
        ids = Remote.objects.values_list('id', flat=True)
        queryset = Key.objects.exclude(id__in=ids)

        return queryset

    list_display = ('name', 'id', )
    readonly_fields = ('id', )

@admin.register(Remote)
class RemoteAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

    list_display = ('name', 'id', )
    readonly_fields = ('id', )

@admin.register(KeyShell)
class KeyShellAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

    list_display = ('name', 'id', )
    readonly_fields = ('id', )
    exclude = ('key', )

@admin.register(RemoteShell)
class RemoteShellAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

    list_display = ('name', 'id', )
    readonly_fields = ('id', )
    exclude = ('remote', )

@admin.register(EmergencyKey)
class EmergencyKeyAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

    list_display = ('name', 'id', )
    readonly_fields = ('id', )

class DistributorKeyInLine(admin.TabularInline):
    model = DistributorKey

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    inlines = [
        DistributorKeyInLine,
    ]

    list_display = ('name', 'code', )
    readonly_fields = ('code', 'id', )
