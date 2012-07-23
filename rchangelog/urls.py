from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'changelog.views.index'),
    url(r'^(?P<changelog_entry_id>\d+)$', 'changelog.views.detail'),
    url(r'^nagyonkiralycsavok/', include(admin.site.urls)),
)
