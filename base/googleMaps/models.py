"""

googleMaps/models.py - builds the google maps image model for the googleMaps app.
The model should handle the downloading once the instance is saved.  So we will
overrider the save() function and handle downloading the google maps image if required.
Then invoke the super save() function.  In order to download the image we will need
to make sure the latitude and longitude are populated and the image field is not yet populated.

"""

from django.db import models
from base import settings
import utils
from utils import download_image, get_next_image_name


class GMImage(models.Model):
    """ 
        The GMImage model represents a google maps image.  The model will handle 
        downloading the image on save 

        The name parameter is for display purposes only.  The image field is the 
        actual image file.  The longitude and latitude are used to locate the 
        center of the image. The url is the url of the google maps image.  The
        date_created and date_modified are the date and time the model was created
        and the last time the model was modified.  The date_created and date_modified
        fields are automatically populated by django.
    """
    name = models.CharField(max_length=255, blank=True, null=True) 
    image = models.ImageField(upload_to=settings.IMAGES_ROOT)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # overriding the save() function to handle downloading the image from google maps
    def save(self, *args, **kwargs):
        # if the image field is not populated and the longitude and latitude are populated then download the image
        if isinstance(self.longitude, float) and isinstance(self.latitude, float) and self.image.name == "":
            # use the util download_image function to download the image 
            self.image = download_image(self.latitude, self.longitude, str(settings.IMAGES_ROOT), get_next_image_name())

        # if the name for the instance is not populated, we will populate it with the name of the image
        # this name is for display purposes only, not for the image field.
        if self.name is None:
            self.name = self.image.name

        # invoking the super save() function will save the model to the database
        super(GMImage, self).save(*args, **kwargs)