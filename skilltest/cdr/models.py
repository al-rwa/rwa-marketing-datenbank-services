from django.db import models

# Create your models here.
from stammdaten.models import Dsgvo, Herkunft, Kommunikationsart, Mandant


class Kunden(models.Model):
    kundeid = models.AutoField(primary_key = True)
    mandant = models.ForeignKey(Mandant, on_delete = models.CASCADE)
    herkunft = models.ForeignKey(Herkunft, null = True, on_delete = models.SET_NULL)
    titel = models.CharField(max_length = 155, null=True, blank=True)
    name = models.CharField(max_length = 755, null = True, blank = True)
    vorname = models.CharField(max_length = 255, null = True, blank = True)
    nachname = models.CharField(max_length = 255, null = True, blank = True)
    geburtsdatum = models.DateField(null = True, blank = True)
    kdkdnr = models.CharField(max_length = 155, null = True, blank = True)
    dsgvo = models.ForeignKey(Dsgvo, null = True, on_delete = models.SET_NULL)
    strasse = models.CharField(max_length=755, null = True, blank = True)
    plz = models.CharField(max_length=25, null = True, blank = True)
    ort = models.CharField(max_length=155, null = True, blank = True)
    email = models.CharField(max_length=255, null = True, blank = True)
    telefon = models.CharField(max_length=255, null = True, blank = True)
    telefon_mobil = models.CharField(max_length=255, null = True, blank = True)
    
    class Meta:
        db_table = 'kuKunden'
        verbose_name = 'Kunde'
        verbose_name_plural = 'Kunden'
    
    def __str__(self):
        return str(self.kundeid)



class Kommunikation(models.Model):
    kundeid = models.ForeignKey(Kunden, related_name="kommunikation", to_field='kundeid', db_column='kundeid',on_delete = models.CASCADE)
    kommunikationsart = models.ForeignKey(Kommunikationsart, on_delete = models.CASCADE, default=1)
    kommunikationswert = models.CharField(max_length = 755, null = True, blank = True)
    
    class Meta:
        db_table = 'kuKommunikation'
        verbose_name = 'Kommunikation'
        verbose_name_plural = 'Kommunikation'
        
    def __str__(self):
        return self.kommunikationswert