# ANMESY
Ein einfaches, anonymes Hinweisgebersystem in Python und Django. Die Meldungen selbst sind über den Adminbereich einsehbar.
Benutzt werden Crispy Forms. Selbstverständlich ist das ganze auch mit den native forms von Django nutzbar.

## Setup

CL:
    mkdir projekt
    cd projekt
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install django
    django-admin startproject django_project
    python3 manage.py migrate
    python3 manage.py startapp meldesystem
    
### settings.py
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "crispy_forms", # ext
        "crispy_bootstrap5", # ext
        "meldesystem.apps.MeldesystemConfig", #int
    ]

### projekt/django_project/urls.py
    from django.urls import path, include
    from django.contrib import admin

    urlpatterns = [
	    path("admin/", admin.site.urls),
	    path("meldesystem/", include("meldesystem.urls")),
    ]

### requirements
    django-crispy-forms==2.0
    crispy-bootstrap5==0.7
