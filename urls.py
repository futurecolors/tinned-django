# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import MEDIA_ROOT, STATIC_ROOT, DEBUG

admin.autodiscover()

handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

urlpatterns = patterns('',

    # Media и стандартные статические файлы
    (r'^_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^(favicon.ico)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    (r'^(robots.txt)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    (r'^(humans.txt)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),

    # Администрирование
    (r'^admin/', include(admin.site.urls)),
    # Sentry
    (r'^sentry/', include('sentry.web.urls')),
    # Admin Tools
 url(r'^admin_tools/', include('admin_tools.urls')),

)

if DEBUG == True:
    urlpatterns += patterns('',
        url(r'^404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^503/$', TemplateView.as_view(template_name='503.html')),
    )

# Приложения
urlpatterns += patterns('', (r'', include('card.urls')))

# Статика
urlpatterns += staticfiles_urlpatterns()