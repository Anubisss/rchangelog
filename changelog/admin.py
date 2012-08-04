from changelog.models import ChangelogEntry, ChangelogLabel, ChangelogLabelEntry
from django.contrib import admin
from django.forms import ModelForm, Textarea

class ChangelogLabelEntryForm(ModelForm):
    class Meta:
        model = ChangelogLabelEntry
        widgets = {
            'content': Textarea(attrs={'cols': 140, 'rows': 3}), # textarea hasznalata
        }

class ChangelogLabelEntryInline(admin.TabularInline):
    model = ChangelogLabelEntry
    extra = 3 # alapbol 3 ures, kitoltheto ChangelogLabelEntry megjelenik
    form = ChangelogLabelEntryForm

class ChangelogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_str', 'ChangelogLabelEntry_Count', 'public', 'PreviewLink') # listazasnal ezek a mezok jelennek meg
    list_display_links = ('id', 'date_str') # mindket oszlop legyen "kattinthato"
    inlines = [ChangelogLabelEntryInline] # ugyanitt listazzuk/szerkesztjuk a ChangelogLabelEntry-ket is

    def make_public(modeladmin, request, queryset):
        queryset.update(public=True)

    def make_unpublic(modeladmin, request, queryset):
        queryset.update(public=False)

    actions = [make_public, make_unpublic] # az admin feluleten (lenyilo menubol) egyszerre tobb bejegyzest lehet (un)publikussa tenni

class ChangelogLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority')
    list_editable = ('name', 'priority') # mar a listazasnal szerkeszthetok a nevek

admin.site.register(ChangelogEntry, ChangelogEntryAdmin)
admin.site.register(ChangelogLabel, ChangelogLabelAdmin)
