"""

googleMaps URL Configuration - handles all url requests for the googleMaps app

"""

from django.urls import path
from . import views

print('googleMaps.urls')
urlpatterns = [
    path('', views.home, name='home'),
    path('get-images', views.get_images, name='get-images'),
    path('refresh-images', views.refresh_images, name='refresh-images')
]