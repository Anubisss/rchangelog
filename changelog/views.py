from django.shortcuts import render_to_response, get_object_or_404, redirect
from changelog.models import ChangelogEntry, ChangelogLabel
from datetime import date
from django.http import Http404
from django.template import RequestContext
from django.conf import settings

def index(request):
    latest_changelog = ChangelogEntry.objects.filter(public=True)
    ym = None
    latest_changelogs = None
    if latest_changelog:
        latest_changelog = latest_changelog.latest() # utolso (datum alapjan) publikus bejegyzes
        ym = date(latest_changelog.date.year, latest_changelog.date.month, 1) # utolso bejegyzesbol a datum kinyerese
        latest_changelogs = ChangelogEntry.objects.filter(date__year=ym.year, date__month=ym.month, public=True) # utolso havi publikus bejegyzesek
    return render_to_response('changelog/index.html', {'latest_changelogs': latest_changelogs, 'ym': ym, 'changelog_explanation': settings.SITE_INDEX_CHANGELOG_EXPLANATION, 'col2': settings.SITE_INDEX_COL2}, context_instance=RequestContext(request))

def archive_all(request):
    changelogs = ChangelogEntry.objects.filter(public=True) # osszes publikus bejegyzes
    fixes_count = 0
    years = list() # evek listaja
    years_months = list() # evek es honapok listaja
    for changelog in changelogs:
        if changelog.date.year not in years: # ez az ev meg nem szerepel a listaban
            years.append(changelog.date.year)
        ym_date = date(changelog.date.year, changelog.date.month, 1) # rendes datum generalasa, nap mindig 1.
        if ym_date not in years_months: # ha az ev es honap meg nem szerepel
            years_months.append(ym_date)
        fixes_count += changelog.ChangelogLabelEntry_Count()
    return render_to_response('changelog/archive_all.html', {'changelogs': changelogs, 'fixes_count': fixes_count, 'years': years, 'years_months': years_months}, context_instance=RequestContext(request))

def archive_year(request, year):
    changelogs = ChangelogEntry.objects.filter(date__year=year, public=True)
    fixes_count = 0
    months = list()
    for changelog in changelogs:
        month = date(int(year), changelog.date.month, 1)
        if month not in months:
            months.append(month)
        fixes_count += changelog.ChangelogLabelEntry_Count()
    return render_to_response('changelog/archive_year.html', {'changelogs': changelogs, 'fixes_count': fixes_count, 'year': year, 'months': months}, context_instance=RequestContext(request))

def archive_month(request, year, month):
    changelogs = ChangelogEntry.objects.filter(date__year=year, date__month=month, public=True)
    fixes_count = 0
    ym_date = date(int(year), int(month), 1)
    for changelog in changelogs:
        fixes_count += changelog.ChangelogLabelEntry_Count()
    return render_to_response('changelog/archive_month.html', {'changelogs': changelogs, 'fixes_count': fixes_count, 'ym': ym_date}, context_instance=RequestContext(request))

def old_url(request, year, month, day):
    return redirect('changelog.views.detail', year=year, month=month, day=day)

def detail(request, year, month, day):
    try:
        changelog_date = date(int(year), int(month), int(day))
    # range error, azaz nincs ilyen nap az adott ev/honapban
    except ValueError:
        raise Http404()
    changelog = get_object_or_404(ChangelogEntry, date=changelog_date)

    if changelog.public == False and not request.user.is_staff: # ha nem publikus akkor csak a staff lathatja
        raise Http404()

    changelog_label_entries = changelog.changeloglabelentry_set.all()

    changelog_label_categorized = list() # ez a lista tartalmazza a ChangelogLabel_Container objektumokat
    for label_entry in changelog_label_entries:
        ChangelogLabel_Container.add(label_entry, changelog_label_categorized)
    changelog_label_categorized.sort()

    return render_to_response('changelog/detail.html', {'changelog': changelog, 'changelog_labels': changelog_label_categorized}, context_instance=RequestContext(request))

# ez az osztaly tarolja az egyes changelog label-hez tartozo bejegyzeseket
# segitsegevel valosul meg, hogy az egy kategoriaba tartozo bejegyzesek
# egy listaba keruljenek
class ChangelogLabel_Container:
    def __init__(self):
        self.changelog_label_entries = list()
        self.changelog_label = ChangelogLabel()

    # eloszor a priority alapjan rendez, csokkeno sorrend
    # majd ha van egyezo priority, akkor a name alapjan (ABC sorrend)
    def __cmp__(self, other):
        cmp_result = cmp(self.changelog_label.priority, other.changelog_label.priority)
        if cmp_result != 0:
            return -cmp_result # ellentetes ertek kell
        else:
            return cmp(self.changelog_label.name, other.changelog_label.name)

    # statikus metodus
    # o hozza letre az uj labeleket vagy adja hozza a bejegyzest mar egy meglevohoz
    @staticmethod
    def add(changelog_label_entry, changelog_label_entries): # params: amit_hozza_adunk, ahova_hozza_adjuk
        label_found = False
        for cl_c in changelog_label_entries:
            if changelog_label_entry.changelog_label_id == cl_c.changelog_label: # egyezes van
                cl_c.changelog_label_entries.append(changelog_label_entry) # a bejegyzes hozzaadasa a mar letezo label-hez
                label_found = True
                break
        if not label_found: # nincs egyezes
            clc = ChangelogLabel_Container() # uj label letrehozasa
            clc.changelog_label = changelog_label_entry.changelog_label_id # majd feltoltese
            clc.changelog_label_entries.append(changelog_label_entry) # ...
            changelog_label_entries.append(clc) # vegul a "globalis" listaba berakas
