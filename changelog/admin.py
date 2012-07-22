from changelog.models import ChangelogEntry, ChangelogLabel, ChangelogLabelEntry
from django.contrib import admin

class ChangelogLabelEntryInline(admin.TabularInline):
    model = ChangelogLabelEntry
    extra = 3 # alapbol 3 ures, kitoltheto ChangelogLabelEntry megjelenik

class ChangelogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_str', 'ChangelogLabelEntry_Count') # listazasnal ezek a mezok jelennek meg
    list_display_links = ('id', 'date_str') # mindket oszlop legyen "kattinthato"
    inlines = [ChangelogLabelEntryInline] # ugyanitt listazzuk/szerkesztjuk a ChangelogLabelEntry-ket is

class ChangelogLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',) # mar a listazasnal szerkeszthetok a nevek

admin.site.register(ChangelogEntry, ChangelogEntryAdmin)
admin.site.register(ChangelogLabel, ChangelogLabelAdmin)
