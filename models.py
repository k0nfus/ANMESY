from django.db import models

class Meldung(models.Model):
    betreff = models.CharField(null=False, max_length=250, verbose_name="Meldegrund")
    text = models.TextField(null=True, max_length=1000, verbose_name="Meldung")
    datum = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Meldungen"
    
    def __str__(self):
        return self.betreff