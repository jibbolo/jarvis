# encoding: utf-8
from django.conf.urls.defaults import *
from jarvis import settings

urlpatterns = patterns('jarvis.views',
    url(r'^$', name="index", view="index"),
)

urlpatterns += patterns('', # STATIC FILES
    (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL, 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)