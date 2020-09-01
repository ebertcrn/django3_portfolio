from django.contrib import admin
from .models import Project # models is in the same folder that this (admin.py) file

# specify what models you want to show in admin page!

admin.site.register(Project) # I want to see this model in my admin page!