from django.db import models

class Meldung(models.Model):
    betreff = models.CharField(null=False, max_length=250)
    text = models.TextField(null=True, max_length=1000)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.betreff