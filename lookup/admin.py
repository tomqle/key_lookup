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
    extra = 0
    ordering = ['vehicle_range']


class DistributorTransponderKeyInLine(admin.TabularInline):
    model = DistributorTransponderKey
    extra = 0
    ordering = ['distributor__name']

@admin.register(TransponderKey)
class TransponderKey(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        DistributorTransponderKeyInLine,
    ]

    def export_as_excel(self, request, queryset):

        timestamp = datetime.now(pytz.timezone('US/Pacific')).strftime('%Y%m%d_%H%M%S')
        filename = 'transponder_key_export_' + timestamp + '.xlsx'
        path = 'static/excel/' + filename

        com = Command()
        com._generate_product_data_output_workbook(queryset, path)

        with open(path, "rb") as excel:
            data = excel.read()

            response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + filename

        return response

    actions = ('export_as_excel',)
    list_display = ('id', 'sku', 'name', 'updated_at', )
    list_display_links = ('id', 'sku', 'name', )
    search_fields = ['id', 'name', 'sku']
    readonly_fields = ('id', 'created_at', 'updated_at', )
    ordering = ['-updated_at']


class DistributorRemoteInLine(admin.TabularInline):
    model = DistributorRemote
    extra = 0
    ordering = ['distributor__name']

@admin.register(Remote)
class RemoteAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        DistributorRemoteInLine,
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
    list_display = ('id', 'sku', 'name', 'updated_at', )
    list_display_links = ('id', 'sku', 'name', )
    search_fields = ['id', 'name', 'sku']
    readonly_fields = ('id', 'created_at', 'updated_at', )
    ordering = ['-updated_at']


class DistributorKeyShellInLine(admin.TabularInline):
    model = DistributorKeyShell
    extra = 0
    ordering = ['distributor__name']


@admin.register(KeyShell)
class KeyShellAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        DistributorKeyShellInLine,
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
    list_display = ('id', 'sku', 'name', 'updated_at', )
    list_display_links = ('id', 'sku', 'name', )
    search_fields = ['id', 'name', 'sku']
    readonly_fields = ('id', 'created_at', 'updated_at', )
    exclude = ('key', )
    ordering = ['-updated_at']


class DistributorRemoteShellInLine(admin.TabularInline):
    model = DistributorRemoteShell
    extra = 0
    ordering = ['distributor__name']

@admin.register(RemoteShell)
class RemoteShellAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        DistributorRemoteShellInLine,
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
    list_display = ('id', 'sku', 'name', 'updated_at', )
    list_display_links = ('id', 'sku', 'name', )
    search_fields = ['id', 'name', 'sku']
    readonly_fields = ('id', 'created_at', 'updated_at', )
    exclude = ('remote', )
    ordering = ['-updated_at']


class DistributorEmergencyKeyInLine(admin.TabularInline):
    model = DistributorEmergencyKey
    extra = 0
    ordering = ['distributor__name']

@admin.register(EmergencyKey)
class EmergencyKeyAdmin(admin.ModelAdmin):
    inlines = [
        VehicleApplicationInLine,
        DistributorEmergencyKeyInLine,
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
    list_display = ('id', 'sku', 'name', 'updated_at', )
    list_display_links = ('id', 'sku', 'name', )
    search_fields = ['id', 'name', 'sku']
    readonly_fields = ('id', 'created_at', 'updated_at', )
    ordering = ['-updated_at']

class DistributorKeyInLine(admin.TabularInline):
    model = DistributorKey

    def get_queryset(self, request):
        remote_ids = Remote.objects.values_list('id', flat=True)
        key_ids = Key.objects.exclude(id__in=remote_ids).values_list('id', flat=True)

        queryset = DistributorKey.objects.filter(key_id__in=key_ids)

        return queryset

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'updated_at', )
    list_display_links = ('id', 'name', 'code', )
    search_fields = ['id', 'name', 'website', 'code']
    readonly_fields = ('id', 'code', 'created_at', 'updated_at', )
    ordering = ['-updated_at']
