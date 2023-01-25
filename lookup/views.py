from django.shortcuts import render
from django.views.generic.base import TemplateView

from lookup.models import Key, Remote, Distributor, DistributorKey, KeyShell, RemoteShell, EmergencyKey, DistributorTransponderKey, DistributorRemote, DistributorKeyShell, DistributorRemoteShell, DistributorEmergencyKey

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ids = Remote.objects.values_list('id', flat=True)

        context = super().get_context_data(**kwargs)
        context['keys'] = Key.objects.order_by('name').exclude(id__in=ids)
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
                if distributors[0].website:
                    context['website'] = distributors[0].website

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
        if self.request.GET.get('d'):
            distributors = Distributor.objects.filter(code=self.request.GET.get('d'))
            if distributors:
                if distributors[0].logo:
                    context['logo_url'] = distributors[0].logo.url
                if distributors[0].website:
                    context['website'] = distributors[0].website

                distributor_remotes = DistributorRemote.objects.filter(distributor=distributors[0], remote=remote)
                if distributor_remotes:
                    context['link'] = distributor_remotes[0].link
                else:
                    context['link'] = distributors[0].website
        return context

class ShellHomeView(TemplateView):
    template_name = 'shell_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shells'] = KeyShell.objects.order_by('id').all()
        return context

class ShellView(TemplateView):
    template_name = 'shell.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shell = KeyShell.objects.get(id=kwargs['id'])
        context['shell'] = shell
        context['vehicles'] = shell.key.vehicleapplication_set.order_by('vehicle_range').all()
        if self.request.GET.get('d'):
            distributors = Distributor.objects.filter(code=self.request.GET.get('d'))
            if distributors:
                if distributors[0].logo:
                    context['logo_url'] = distributors[0].logo.url
                if distributors[0].website:
                    context['website'] = distributors[0].website

                distributor_key_shells = DistributorKeyShell.objects.filter(distributor=distributors[0], key_shell=shell)
                if distributor_key_shells:
                    context['link'] = distributor_key_shells[0].link
                else:
                    context['link'] = distributors[0].website
        return context

class KeyShellHomeView(TemplateView):
    template_name = 'key_shell_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key_shells'] = KeyShell.objects.order_by('id').all()
        return context

class KeyShellView(TemplateView):
    template_name = 'key_shell.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key_shell = KeyShell.objects.get(id=kwargs['id'])
        context['key_shell'] = key_shell
        context['vehicles'] = key_shell.vehicleapplication_set.order_by('vehicle_range').all()
        if self.request.GET.get('d'):
            distributors = Distributor.objects.filter(code=self.request.GET.get('d'))
            if distributors:
                if distributors[0].logo:
                    context['logo_url'] = distributors[0].logo.url
                if distributors[0].website:
                    context['website'] = distributors[0].website

                distributor_key_shells = DistributorKeyShell.objects.filter(distributor=distributors[0], key_shell=key_shell)
                if distributor_key_shells:
                    context['link'] = distributor_key_shells[0].link
                else:
                    context['link'] = distributors[0].website

        return context

class RemoteShellHomeView(TemplateView):
    template_name = 'remote_shell_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['remote_shells'] = RemoteShell.objects.order_by('id').all()
        return context

class RemoteShellView(TemplateView):
    template_name = 'remote_shell.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        remote_shell = RemoteShell.objects.get(id=kwargs['id'])
        context['remote_shell'] = remote_shell
        context['vehicles'] = remote_shell.vehicleapplication_set.order_by('vehicle_range').all()
        if self.request.GET.get('d'):
            distributors = Distributor.objects.filter(code=self.request.GET.get('d'))
            if distributors:
                if distributors[0].logo:
                    context['logo_url'] = distributors[0].logo.url
                if distributors[0].website:
                    context['website'] = distributors[0].website

                distributor_remote_shells = DistributorRemoteShell.objects.filter(distributor=distributors[0], remote_shell=remote_shell)
                if distributor_remote_shells:
                    context['link'] = distributor_remote_shells[0].link
                else:
                    context['link'] = distributors[0].website

        return context

class EmergencyKeyHomeView(TemplateView):
    template_name = 'emergency_key_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emergency_keys'] = EmergencyKey.objects.order_by('id').all()
        return context

class EmergencyKeyView(TemplateView):
    template_name = 'emergency_key.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        emergency_key = EmergencyKey.objects.get(id=kwargs['id'])
        context['emergency_key'] = emergency_key
        context['vehicles'] = emergency_key.vehicleapplication_set.order_by('vehicle_range').all()
        if self.request.GET.get('d'):
            distributors = Distributor.objects.filter(code=self.request.GET.get('d'))
            if distributors:
                if distributors[0].logo:
                    context['logo_url'] = distributors[0].logo.url
                if distributors[0].website:
                    context['website'] = distributors[0].website

                distributor_emergency_keys = DistributorEmergencyKey.objects.filter(distributor=distributors[0], emergency_key=emergency_key)
                if distributor_emergency_keys:
                    context['link'] = distributor_emergency_keys[0].link
                else:
                    context['link'] = distributors[0].website

        return context