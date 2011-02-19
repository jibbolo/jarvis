# encoding: utf-8
from django.conf.urls.defaults import *
from jarvis import settings

urlpatterns = patterns('jarvis.views',
    url(r'^$', name="index", view="index"),
)

urlpatterns += patterns('', 
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login' ),
    # STATIC FILES
    (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL, 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)