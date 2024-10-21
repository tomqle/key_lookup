from django.contrib import admin
from django.http import HttpResponse

from lookup.forms import DistributorImportForm, DistributorConfirmImportForm
from lookup.models import Key, Remote, VehicleApplication, Distributor, DistributorKey, KeyShell, RemoteShell, EmergencyKey, TransponderKey, DistributorTransponderKey, DistributorRemote, DistributorKeyShell, DistributorRemoteShell, DistributorEmergencyKey
from lookup.management.commands.import_product_data import Command

from datetime import datetime
#from import_export import resources
#from import_export.admin import ImportExportModelAdmin, ImportMixin
import pytz

# Register your models here.

'''
# import_export resources
class TransponderKeyResource(resources.ModelResource):
    class Meta:
        model = TransponderKey;

class DistributorTransponderKeyResource(resources.ModelResource):
    class Meta:
        model = DistributorTransponderKey;
'''


class VehicleApplicationInLine(admin.TabularInline):
    model = VehicleApplication
    fields = ('vehicle_range',)

#@admin.register(Key)
#class KeyAdmin(admin.ModelAdmin):
    #inlines = [
        #VehicleApplicationInLine,
        #]
    #def get_queryset(self, request):
        #ids = Remote.objects.values_list('id', flat=True)
        #queryset = Key.objects.exclude(id__in=ids)

        #return queryset
    
    #def export_as_excel(self, request, queryset):

        #timestamp = datetime.now(pytz.timezone('US/Pacific')).strftime('%Y%m%d_%H%M%S')
        #filename = 'key_export_' + timestamp + '.xlsx'
        #path = 'static/excel/' + filename

        #com = Command()
        #com._generate_product_data_output_workbook(queryset, path)

        #with open(path, "rb") as excel:
            #data = excel.read()

            #response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            #response['Content-Disposition'] = 'attachment; filename=' + filename

        #return response

    #actions = ('export_as_excel',)
    #list_display = ('name', 'id', )
    #readonly_fields = ('id', )

@admin.register(TransponderKey)
class TransponderKeyAdmin(admin.ModelAdmin):
#class TransponderKeyAdmin(ImportExportModelAdmin):
    #resource_classes = [TransponderKeyResource]

    inlines = [
        VehicleApplicationInLine,
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
    ordering = ('transponder_key__id', 'id', )

class DistributorRemoteInLine(admin.TabularInline):
    model = DistributorRemote
    ordering = ('remote__id', 'id', )

class DistributorKeyShellInLine(admin.TabularInline):
    model = DistributorKeyShell
    ordering = ('key_shell__id', 'id', )

class DistributorRemoteShellInLine(admin.TabularInline):
    model = DistributorRemoteShell
    ordering = ('remote_shell__id', 'id', )

class DistributorEmergencyKeyInLine(admin.TabularInline):
    model = DistributorEmergencyKey
    ordering = ('emergency_key__id', 'id', )

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    inlines = [
        DistributorTransponderKeyInLine,
        DistributorRemoteInLine,
        DistributorKeyShellInLine,
        DistributorRemoteShellInLine,
        DistributorEmergencyKeyInLine,
    ]

    list_display = ('name', 'code', )
    readonly_fields = ('code', 'id', )

'''
@admin.register(DistributorTransponderKey)
#class DistributorTransponderKeyAdmin(ImportExportModelAdmin):
class DistributorTransponderKeyAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['distributor__name', 'transponder_key_id', 'transponder_key__name', 'link']
    list_filter = ['distributor__name']

    resource_classes = [DistributorTransponderKeyResource]
    import_form_class = DistributorImportForm
    confirm_form_class = DistributorConfirmImportForm

    def get_confirm_form_initial(self, request, import_form):
        print ('get_confirm_form_initial')
        initial = super().get_confirm_form_initial(request, import_form)

        print(initial)
        print(import_form)
        print(import_form.cleaned_data['distributor'])

        # Pass on the `author` value from the import form to
        # the confirm form (if provided)
        if import_form:
            initial['distributor'] = import_form.cleaned_data['distributor'].id
        return initial

    def get_import_data_kwargs(self, request, *args, **kwargs):
        print('kwargs: ')
        print(kwargs)
        form = kwargs.get("form", None)
        print(form)
        if form and hasattr(form, "cleaned_data"):
            kwargs.update({"distributor": form.cleaned_data.get("distributor", None)})
        return kwargs
    
    def after_init_instance(self, instance, new, row, **kwargs):
        print ('after_init_instance')
        if "distributor" in kwargs:
            instance.distributor = kwargs["distributor"]
'''