from django.contrib import admin

# Register the GMimage model with the admin site
from .models import GMImage
admin.site.register(GMImage)