from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'changelog.views.index'),
    url(r'^(?P<year>\d{4})/$', 'changelog.views.archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>0[1-9]|1[0-2])/$', 'changelog.views.archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>0[1-9]|1[0-2])/(?P<day>0[1-9]|[12][0-9]|3[0-1])/$', 'changelog.views.detail'),
    url(r'^(?P<year>\d{4})_(?P<month>0[1-9]|1[0-2])_(?P<day>0[1-9]|[12][0-9]|3[0-1]).html$', 'changelog.views.detail'), # regi tipusu URL-ek kiszolgalasa, 2011_03_02.html
    url(r'^nagyonkiralycsavok/', include(admin.site.urls)),
)
