from django.test import TestCase
from googleMaps.models import GMImage
from base import settings


class TestGMImage(TestCase):
    """
    A class to test the Google Maps Image model

    Attributes
    ----------
    image : The GMImage model test instance

    
    Methods
    -------
    test_model_save_image_download()
        tests that the GMImage model saves properly

    The setUp / test method breakdown is based on the following article:
    https://docs.djangoproject.com/en/4.1/topics/testing/overview/
    

    """
    image = None

    def setUp(self):
        """ use the predefined settings to isolate a specific image to download from Google Maps """
        self.image = GMImage.objects.create(
            longitude=settings.PASADENA_CORNER_CORDS['coordinates'][0]["LONG"],
            latitude=settings.PASADENA_CORNER_CORDS['coordinates'][0]["LAT"],
            name=settings.PASADENA_CORNER_CORDS['coordinates'][0]["NAME"]
        )

    def test_model_save_image_download(self):   
        """ this test will invoke the save method in the GMImage model 
        instance created in the setup.  Once invoked the save method 
        will trigger downloading the image from Google Maps.  A confirmation 
        that the size of the image matches the predefined settings 
        will complete the test."""     
        self.image.save()
        self.assertEqual(self.image.image.width, settings.GOOGLE_MAPS_SIZE_X)
        self.assertEqual(self.image.image.height, settings.GOOGLE_MAPS_SIZE_Y)
        # delete the image from the media/images directory
        self.image.image.delete()