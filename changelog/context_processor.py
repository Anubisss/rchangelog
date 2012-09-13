from changelog.models import ChangelogEntry
from django.conf import settings

def my_context_processor(request):
    latest_changelog = ChangelogEntry.objects.latest(field_name='date') # TODO: public
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_FOOTER_ADDRESS': settings.SITE_FOOTER_ADDRESS,
        'latest_changelog': latest_changelog
    }
