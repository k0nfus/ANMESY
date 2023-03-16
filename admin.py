from django.contrib import admin

from .models import Meldung

class MeldungAdmin(admin.ModelAdmin):
    list_display = ("datum", "betreff", "text",)    

admin.site.register(Meldung, MeldungAdmin)