from django.shortcuts import render_to_response
from changelog.models import ChangelogEntry

def index(request):
    changelogs = ChangelogEntry.objects.all()
    return render_to_response('changelog/index.html', {'changelogs': changelogs})

def detail(request, changelog_entry_id):
    changelog = ChangelogEntry.objects.get(pk=changelog_entry_id)
    return render_to_response('changelog/detail.html', {'changelog': changelog})
