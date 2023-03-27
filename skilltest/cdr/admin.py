# Register your models here.
from cdr.models import Kommunikation, Kunden
from django.contrib import admin
from django.db import connection


class KundenAdmin(admin.ModelAdmin):
    list_display = ["kdkdnr","name","vorname","nachname","strasse","plz","ort","email","telefon","telefon_mobil"]
    fields = ["mandant","herkunft","titel","name","vorname","nachname","geburtsdatum","kdkdnr","dsgvo","strasse","plz","ort","email","telefon","telefon_mobil"]
    actions = ["set_dsgvo_02",]
    
    
    def set_dsgvo_02(self, request, queryset):
        
        for obj in queryset:
            objid = obj.kundeid
            cursor = connection.cursor()
            try:
                cursor.execute(f'update kuKunden set dsgvo_id = 2 where kundeid = {objid} ;')
            finally:
                cursor.close()
    
    set_dsgvo_02.short_description = 'Kunden auf 02 abgelehnt setzen'


class KommunikationAdmin(admin.ModelAdmin):
    fields = ["__all__"]

admin.site.register(Kunden, KundenAdmin)
admin.site.register(Kommunikation, KommunikationAdmin)