""" 

base URL Configuration - for now only admin is needed in this configuration 
file.  All other urls are in the googleMaps app.  The static media URL configuration
is added to the end of the urlpatterns list so that images on the file system 
are handled properly.  See the following article for more information on file handling:
https://docs.djangoproject.com/en/4.1/howto/static-files/

"""
from django.contrib import admin
from django.urls import path, include
from base import settings
from django.conf.urls.static import static

print('base.urls')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('googleMaps.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
