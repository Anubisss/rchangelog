from django.db import models
from django.core.validators import MaxValueValidator
from django.core.urlresolvers import reverse

# changelog bejegyzes, "oldal"
class ChangelogEntry(models.Model):
    date = models.DateField(unique=True) # a changelog bejegyzes "cime"
    public = models.BooleanField() # a bejegyzes lathato-e mindenki szamara
    custom_like_url = models.CharField(max_length=64, blank=True) # Facebook like gombhoz tartozo sajat URL

    def __unicode__(self):
        return self.date.__str__()

    # "szep" abrazolasa a datumnak
    def date_str(self):
        return self.date.strftime('%Y. %m. %d.')
    date_str.short_description = 'Date' # ez a nev jelenik meg az admin feluleten az oszlopnal

    # vissza adja hany ChangelogLabelEntry tartozik ide
    def ChangelogLabelEntry_Count(self):
        return self.changeloglabelentry_set.count()
    ChangelogLabelEntry_Count.short_description = 'ChangelogLabelEntry Count'

    # elonezeti link generalasa
    # meg nem publikus bejegyzesek ellenorzesekor jol jon
    def PreviewLink(self):
        return '<a href="%s" target="_blank">%s</a>' % (reverse('changelog.views.detail', kwargs={'year': self.date.strftime('%Y'), 'month': self.date.strftime('%m'), 'day': self.date.strftime('%d')}), self.date_str())
    PreviewLink.allow_tags = True # HTML tagok engedelyezese, igy nincs escape-eles az admin feluleten
    PreviewLink.short_description = 'Preview'

    class Meta:
        db_table = 'changelog_entry' # table nev felulirasa, changelog_changelogentry helyett
        ordering = ['-date'] # csokkeno sorrendu rendezes, azaz a legujabb datum lesz legelol
        get_latest_by = 'date' # datum alapjan kerjuk le az utolso entryt, latest()

# egy changelog kategoria
# ez ala kerulnek majd az egyes sorok a changelog oldalon
class ChangelogLabel(models.Model):
    name = models.CharField(max_length=64, unique=True) # a label neve, pl.: Egyeb, Event, Druid
    priority = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)]) # 0-100

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'changelog_label'
        ordering = ['-priority', 'name'] # rendezes prioritas (csokkeno sorrend), majd nev (ABC sorrend) alapjan

# changelog kategoriahoz bejegyzes
# lista elem es a ChangelogLabel a lista "cime"
class ChangelogLabelEntry(models.Model):
    content = models.CharField(max_length=512, help_text="BBCode:\n\n- [url]http://domain.hu/\n- [url=http://domain.hu/]domain link[/url]\n- [b]felkover[/b]\n- [u]alahuzott[/u]\n- [i]dolt[/i]") # valodi tartalom, pl.: x spell javitva
    changelog_entry_id = models.ForeignKey(ChangelogEntry, db_column='changelog_entry_id') # a bejegyzes melyik changeloghoz tartozik
    changelog_label_id = models.ForeignKey(ChangelogLabel, db_column='changelog_label_id') # a bejegyzes melyik kategoriahoz tartozik

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'changelog_label_entry'
