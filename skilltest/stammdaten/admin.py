from django.contrib import admin

# Register your models here.
from stammdaten.models import Dsgvo, Herkunft, Kommunikationsart, Mandant

admin.site.register(Mandant)
admin.site.register(Herkunft)
admin.site.register(Kommunikationsart)
admin.site.register(Dsgvo)