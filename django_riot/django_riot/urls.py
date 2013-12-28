from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_riot.views.home', name='home'),
    url(r'^', include('riot_api.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
