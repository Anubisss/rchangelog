from django.db import models

# changelog bejegyzes, "oldal"
class ChangelogEntry(models.Model):
    date = models.DateField() # a changelog bejegyzes "cime"

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

    class Meta:
        db_table = 'changelog_entry' # table nev felulirasa, changelog_changelogentry helyett

# egy changelog kategoria
# ez ala kerulnek majd az egyes sorok a changelog oldalon
class ChangelogLabel(models.Model):
    name = models.CharField(max_length=64, unique=True) # a label neve, pl.: Egyeb, Event, Druid

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'changelog_label'
        ordering = ['name'] # rendezes nev alapjan, ABC sorrend

# changelog kategoriahoz bejegyzes
# lista elem es a ChangelogLabel a lista "cime"
class ChangelogLabelEntry(models.Model):
    content = models.CharField(max_length=512) # valodi tartalom, pl.: x spell javitva
    changelog_entry_id = models.ForeignKey(ChangelogEntry, db_column='changelog_entry_id') # a bejegyzes melyik changeloghoz tartozik
    changelog_label_id = models.ForeignKey(ChangelogLabel, db_column='changelog_label_id') # a bejegyzes melyik kategoriahoz tartozik

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'changelog_label_entry'

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=96, unique=True)
    sha_pass_hash = models.CharField(max_length=120)

    class Meta:
        db_table = 'account'
        managed = False # nincs letrehozas syncnel, mivel ez mar egy letezo account table
