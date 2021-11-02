from django.shortcuts import render
from django.views.generic.base import TemplateView

from lookup.models import Key, Remote

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

class RemoteHomeView(TemplateView):
    template_name = 'remote_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['remotes'] = Remote.objects.order_by('id').all()
        return context

class RemoteView(TemplateView):
    template_name = 'remote.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        remote = Remote.objects.get(id=kwargs['id'])
        context['remote'] = remote
        context['vehicles'] = remote.vehicleapplication_set.order_by('vehicle_range').all()
        return context

