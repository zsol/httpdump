from django.conf.urls import patterns, include, url
from django.conf import settings
from httpdump.views import home


urlpatterns = patterns('',
    url(r'^$', home),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
