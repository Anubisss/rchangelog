from django.conf.urls import patterns, include, url
from django.contrib import admin

# changelog app-hoz tartozo view-ek URL-jei
urlpatterns = patterns('changelog.views',
    url(r'^$', 'index'),
    url(r'^all/$', 'archive_all'),
    url(r'^(?P<year>\d{4})/$', 'archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>0[1-9]|1[0-2])/$', 'archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>0[1-9]|1[0-2])/(?P<day>0[1-9]|[12][0-9]|3[0-1])/$', 'detail'),
    url(r'^(?P<year>\d{4})_(?P<month>0[1-9]|1[0-2])_(?P<day>0[1-9]|[12][0-9]|3[0-1]).html$', 'old_url'), # regi tipusu URL-ek atiranyitasa, 2011_03_02.html
)

admin.autodiscover()

urlpatterns += patterns('',
    url(r'^legnagyobbkiralycsavok/', include(admin.site.urls)), # Django default admin oldalanak elerhetosege
)
