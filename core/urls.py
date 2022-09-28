"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('frontend.urls')),
    path('sw.js', (TemplateView.as_view(template_name='pwa/sw.js', content_type='application/javascript')), name='sw.js'),
    path('offline/', (TemplateView.as_view(template_name='pwa/offline.html')), name='offline'),
    path('robots.txt', (TemplateView.as_view(
        template_name='pwa/robots.txt')), name='robots.txt')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Strakon SuperAdmin"
admin.site.site_title = "Strakon"
# admin.site.index_title = "Strakon SuperAdmin"