from django.urls import path
from .views import meldung

urlpatterns = [
	path("", meldung, name="meldung"),
]