from django.db import models

# Create your models here.

class Mandant(models.Model):
    mandant_id = models.BigAutoField("MandantID", primary_key=True)
    nr = models.PositiveIntegerField("Mandant-Nr", unique = True)
    name = models.CharField("Mandant", max_length=255, unique = True)
    aktiv = models.BooleanField("Aktiv?", default=False)
    class Meta:
        db_table = "sdMandant"
        verbose_name_plural = "Mandanten"
        ordering = ["nr",]

    def __str__(self):
        return f"{self.nr} - {self.name}"
    


class Herkunft(models.Model):
    herkunft_id = models.BigAutoField("HerkunftID", primary_key=True)
    slug = models.SlugField("Kürzel", unique=True)
    name = models.CharField("Herkunft", max_length=255, unique = True)
    aktiv = models.BooleanField("Aktiv?", default=False)

    class Meta:
        db_table = "sdHerkunft"
        verbose_name_plural = "Herkunft"
        ordering = ["slug",]

    def __str__(self):
        return f"{self.slug} ({self.name})"


class Kommunikationsart(models.Model):
    kuerzel = models.CharField(max_length=20)
    beschreibung = models.CharField(max_length=150)

    class Meta:
        db_table = 'sdKommunikationsart'
        verbose_name_plural = "Kommunikationsarten"
        
    def __str__(self):
        return self.kuerzel
    
    
class Dsgvo(models.Model):
    dsgvo_kz = models.CharField(max_length=2)
    dsgvo_beschreibung = models.CharField(max_length=100)
    newsletter_upload = models.BooleanField(default=False, null=False, blank=False)
    matching_mandantenuebergreifend = models.BooleanField(default=False, blank=False)
    
    class Meta:
        db_table = 'sdDsgvo'
        verbose_name_plural = "dsgvo"
        
    def __str__(self):
        return self.dsgvo_kz + ' (' + self.dsgvo_beschreibung + ')'