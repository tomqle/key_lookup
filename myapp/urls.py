"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from lookup.views import HomeView, KeyView, RemoteHomeView, RemoteView

admin.site.site_header = "Keys Lookup Admin"
admin.site.site_title = "Keys Lookup Portal"
admin.site.index_title = "Welcome to the Keys Lookup Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('keys/', HomeView.as_view(), name='home'),
    path('keys/<int:id>/', KeyView.as_view(), name='key'),
    path('remotes/', RemoteHomeView.as_view(), name='remote_home'),
    path('remotes/<int:id>/', RemoteView.as_view(), name='remote'),
    path('/', RedirectView.as_view(url='keys/', permanent=False), name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
