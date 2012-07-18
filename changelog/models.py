from django.db import models

# changelog bejegyzes, "oldal"
class ChangelogEntry(models.Model):
    date = models.DateField() # a changelog bejegyzes "cime"
    created = models.DateTimeField(auto_now_add=True) # amikor a bejegyzes letrejott
    publisher_accid = models.PositiveIntegerField() # a bekuldo account ID-je

    class Meta:
        db_table = 'changelog_entry' # table nev felulirasa, changelog_changelogentry helyett

# egy changelog kategoria
# ez ala kerulnek majd az egyes sorok a changelog oldalon
class ChangelogLabel(models.Model):
    name = models.CharField(max_length=64, unique=True) # a label neve, pl.: Egyeb, Event, Druid

    class Meta:
        db_table = 'changelog_label'

# changelog kategoriahoz bejegyzes
# lista elem es a ChangelogLabel a lista "cime"
class ChangelogLabelEntry(models.Model):
    content = models.CharField(max_length=512) # valodi tartalom, pl.: x spell javitva
    changelog_entry_id = models.ForeignKey(ChangelogEntry) # a bejegyzes melyik changeloghoz tartozik
    changelog_label_id = models.ForeignKey(ChangelogLabel) # a bejegyzes melyik kategoriahoz tartozik

    class Meta:
        db_table = 'changelog_label_entry'
