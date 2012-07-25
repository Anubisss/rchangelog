from django.shortcuts import render_to_response, get_object_or_404
from changelog.models import ChangelogEntry, ChangelogLabel

def index(request):
    changelogs = ChangelogEntry.objects.filter(public=True)
    return render_to_response('changelog/index.html', {'changelogs': changelogs})

def detail(request, changelog_entry_id):
    changelog = get_object_or_404(ChangelogEntry, pk=changelog_entry_id, public=True)
    changelog_label_entries = changelog.changeloglabelentry_set.all()

    changelog_label_categorized = list() # ez a lista tartalmazza a ChangelogLabel_Container objektumokat
    for label_entry in changelog_label_entries:
        ChangelogLabel_Container.add(label_entry, changelog_label_categorized)

    return render_to_response('changelog/detail.html', {'changelog': changelog, 'changelog_labels': changelog_label_categorized})

# ez az osztaly tarolja az egyes changelog label-hez tartozo bejegyzeseket
# segitsegevel valosul meg, hogy az egy kategoriaba tartozo bejegyzesek
# egy listaba keruljenek
class ChangelogLabel_Container:
    def __init__(self):
        self.changelog_label_entries = list()
        self.changelog_label = ChangelogLabel()

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
