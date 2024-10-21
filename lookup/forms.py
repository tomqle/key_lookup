from django.forms import ModelChoiceField

from lookup.models import Distributor

from import_export.forms import ImportForm, ConfirmImportForm;

class DistributorImportForm(ImportForm):
    distributor = ModelChoiceField(
        queryset=Distributor.objects.all(),
        required=True)

class DistributorConfirmImportForm(ConfirmImportForm):
    distributor = ModelChoiceField(
        queryset=Distributor.objects.all(),
        required=True)