from django.contrib import admin
from .models import vehicles_DB,vehicles_DBAdmin
admin.site.register(vehicles_DB,vehicles_DBAdmin)