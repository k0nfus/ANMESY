from django import forms
from .models import Meldung

class MeldungForm(forms.ModelForm):
    class Meta:
        model = Meldung
        fields = ("betreff", "text",)