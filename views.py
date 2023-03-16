from django.shortcuts import render
from .forms import MeldungForm
from django.http import HttpResponseRedirect
from django.contrib import messages

def meldung(request):
    form = MeldungForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Ihre Meldung wurde erfolgreich und anonym eingereicht!")
        return HttpResponseRedirect("/meldesystem")
    context = {
        "form":form
    }
    return render(request, "meldung.html", context)