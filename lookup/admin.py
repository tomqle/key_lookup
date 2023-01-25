from django.contrib import admin
from django.http import HttpResponse
from lookup.models import Key, Remote, VehicleApplication, Distributor, DistributorKey, KeyShell, RemoteShell, EmergencyKey, TransponderKey, DistributorTransponderKey, DistributorRemote, DistributorKeyShell, DistributorRemoteShell, DistributorEmergencyKey
from lookup.management.commands.import_product_data import Command

from datetime import datetime
import pytz

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
    
    def export_as_excel(self, request, queryset):

        timestamp = datetime.now(pytz.timezone('US/Pacific')).strftime('%Y%m%d_%H%M%S')
        filename = 'key_export_' + timestamp + '.xlsx'
        path = 'static/excel/' + filename

        com = Command()
        com._generate_product_data_output_workbook(queryset, path)

        with open(path, "rb") as excel:
            data = excel.read()

            response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + filename

        return response

    actions = ('export_as_excel',)
    list_display = ('name', 'id', )
    readonly_fields = ('id', )

@admin.register(Remote)
class RemoteAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

    def export_as_excel(self, request, queryset):
        timestamp = datetime.now(pytz.timezone('US/Pacific')).strftime('%Y%m%d_%H%M%S')
        filename = 'remote_export_' + timestamp + '.xlsx'
        path = 'static/excel/' + filename

        com = Command()
        com._generate_product_data_output_workbook(queryset, path)

        with open(path, "rb") as excel:
            data = excel.read()

            response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + filename

        return response

    actions = ('export_as_excel',)
    list_display = ('name', 'id', )
    readonly_fields = ('id', )

@admin.register(KeyShell)
class KeyShellAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

    def export_as_excel(self, request, queryset):
        timestamp = datetime.now(pytz.timezone('US/Pacific')).strftime('%Y%m%d_%H%M%S')
        filename = 'key_shell_export_' + timestamp + '.xlsx'
        path = 'static/excel/' + filename

        com = Command()
        com._generate_product_data_output_workbook(queryset, path)

        with open(path, "rb") as excel:
            data = excel.read()

            response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + filename

        return response

    actions = ('export_as_excel',)
    list_display = ('name', 'id', )
    readonly_fields = ('id', )
    exclude = ('key', )

@admin.register(RemoteShell)
class RemoteShellAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

    def export_as_excel(self, request, queryset):
        timestamp = datetime.now(pytz.timezone('US/Pacific')).strftime('%Y%m%d_%H%M%S')
        filename = 'remote_shell_export_' + timestamp + '.xlsx'
        path = 'static/excel/' + filename

        com = Command()
        com._generate_product_data_output_workbook(queryset, path)

        with open(path, "rb") as excel:
            data = excel.read()

            response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + filename

        return response

    actions = ('export_as_excel',)
    list_display = ('name', 'id', )
    readonly_fields = ('id', )
    exclude = ('remote', )

@admin.register(EmergencyKey)
class EmergencyKeyAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        ]

    def export_as_excel(self, request, queryset):
        timestamp = datetime.now(pytz.timezone('US/Pacific')).strftime('%Y%m%d_%H%M%S')
        filename = 'emergency_key_export_' + timestamp + '.xlsx'
        path = 'static/excel/' + filename

        com = Command()
        com._generate_product_data_output_workbook(queryset, path)

        with open(path, "rb") as excel:
            data = excel.read()

            response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + filename

        return response

    actions = ('export_as_excel',)
    list_display = ('name', 'id', )
    readonly_fields = ('id', )

class DistributorKeyInLine(admin.TabularInline):
    model = DistributorKey

    def get_queryset(self, request):
        remote_ids = Remote.objects.values_list('id', flat=True)
        key_ids = Key.objects.exclude(id__in=remote_ids).values_list('id', flat=True)

        queryset = DistributorKey.objects.filter(key_id__in=key_ids)

        return queryset

class DistributorTransponderKeyInLine(admin.TabularInline):
    model = DistributorTransponderKey

class DistributorRemoteInLine(admin.TabularInline):
    model = DistributorRemote

class DistributorKeyShellInLine(admin.TabularInline):
    model = DistributorKeyShell

class DistributorRemoteShellInLine(admin.TabularInline):
    model = DistributorRemoteShell

class DistributorEmergencyKeyInLine(admin.TabularInline):
    model = DistributorEmergencyKey

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    inlines = [
        DistributorKeyInLine,
        #DistributorTransponderKeyInLine,
        #DistributorRemoteInLine,
        #DistributorKeyShellInLine,
        #DistributorRemoteShellInLine,
        #DistributorEmergencyKeyInLine,
    ]

    list_display = ('name', 'code', )
    readonly_fields = ('code', 'id', )
