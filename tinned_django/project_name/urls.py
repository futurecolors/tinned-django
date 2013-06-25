# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings


admin.autodiscover()


handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'


urlpatterns = patterns('',
    (r'^(favicon.ico)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^(robots.txt)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^(humans.txt)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    (r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# We need to see these pages in development
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    )

# Apps
urlpatterns += patterns('',
    # here goes
)

# Staticfiles
urlpatterns += staticfiles_urlpatterns()
