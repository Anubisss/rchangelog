from changelog.models import ChangelogEntry, ChangelogLabel, ChangelogLabelEntry
from django.contrib import admin

admin.site.register(ChangelogEntry)
admin.site.register(ChangelogLabel)
admin.site.register(ChangelogLabelEntry)
