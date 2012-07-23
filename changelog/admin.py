from changelog.models import ChangelogEntry, ChangelogLabel, ChangelogLabelEntry
from django.contrib import admin

class ChangelogLabelEntryInline(admin.TabularInline):
    model = ChangelogLabelEntry
    extra = 3 # alapbol 3 ures, kitoltheto ChangelogLabelEntry megjelenik

class ChangelogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_str', 'ChangelogLabelEntry_Count', 'public') # listazasnal ezek a mezok jelennek meg
    list_display_links = ('id', 'date_str') # mindket oszlop legyen "kattinthato"
    inlines = [ChangelogLabelEntryInline] # ugyanitt listazzuk/szerkesztjuk a ChangelogLabelEntry-ket is

    def make_public(modeladmin, request, queryset):
        queryset.update(public=True)

    def make_unpublic(modeladmin, request, queryset):
        queryset.update(public=False)

    actions = [make_public, make_unpublic] # az admin feluleten (lenyiolo menubol) egyszerre tobb bejegyzest lehet (un)publikussa tenni

class ChangelogLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',) # mar a listazasnal szerkeszthetok a nevek

admin.site.register(ChangelogEntry, ChangelogEntryAdmin)
admin.site.register(ChangelogLabel, ChangelogLabelAdmin)
