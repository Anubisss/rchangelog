from django.shortcuts import render_to_response, get_object_or_404
from changelog.models import ChangelogEntry

def index(request):
    changelogs = ChangelogEntry.objects.filter(public=True)
    return render_to_response('changelog/index.html', {'changelogs': changelogs})

def detail(request, changelog_entry_id):
    changelog = get_object_or_404(ChangelogEntry, pk=changelog_entry_id, public=True)
    return render_to_response('changelog/detail.html', {'changelog': changelog})
