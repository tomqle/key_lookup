from django.shortcuts import render
from django.views.generic.base import TemplateView

from lookup.models import Key

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keys'] = Key.objects.order_by('name').all()
        return context

class KeyView(TemplateView):
    template_name = 'key.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = Key.objects.get(id=kwargs['id'])
        context['key'] = key
        context['vehicles'] = key.vehicleapplication_set.order_by('vehicle_range').all()
        return context

