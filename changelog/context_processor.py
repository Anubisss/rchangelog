from changelog.models import ChangelogEntry
from django.conf import settings

# sajat context processor
# segitsegevel megoldhato, hogy ezek a parameterek minden egyes template-nek
# atadodjanak ha a template render-nel van context instance megadva
def my_context_processor(request):
    latest_changelog = ChangelogEntry.objects.filter(public=True) # osszes publikus bejegyzes
    if latest_changelog: # ha vannak bejegyzesek
        latest_changelog = latest_changelog.latest() # legutolso bejegyzes
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_FOOTER_ADDRESS': settings.SITE_FOOTER_ADDRESS,
        'SITE_URL': settings.SITE_URL,
        'LATEST_CHANGELOG': latest_changelog
    }
