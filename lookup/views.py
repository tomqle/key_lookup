from django.shortcuts import render
from django.views.generic.base import TemplateView

from lookup.models import Key, Remote, Distributor, DistributorKey

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
        if self.request.GET.get('d'):
            distributors = Distributor.objects.filter(code=self.request.GET.get('d'))
            if distributors:
                if distributors[0].logo:
                    context['logo_url'] = distributors[0].logo.url
                distributor_keys = DistributorKey.objects.filter(distributor=distributors[0], key=key)
                if distributor_keys:
                    context['link'] = distributor_keys[0].link
                else:
                    context['link'] = distributors[0].website
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

