from django.shortcuts import render
from base import settings
import os
from .models import GMImage
import os


def get_pasadena_corner_images():
    """ 
        get_pasadena_corner_images

        Reads the settings files for the 4 corners of Pasadena, CA and downloads the google maps images.
        This function knows nothing of the mechanics of the API or how to download the images.  This is 
        all contained in the model's save method.  We simply have to create an instance of the model and
        call the save method.  The save method will download the image and save it to the database.
    """
    images = []

    # get the image data from the settings file
    for image_data in settings.PASADENA_CORNER_CORDS['coordinates']:
        # get the latitude and longitude
        latitude = image_data["LAT"]
        longitude = image_data["LONG"]
        name = image_data["NAME"]
        # create a blank GMImage model
        new_image = GMImage()
        new_image.name = name
        new_image.latitude = latitude
        new_image.longitude = longitude
        new_image.save()
            
        # add the image to the images list
        images.append(new_image)
        
    # return the images list
    return images


def home(request):
    """
        home(request)

        A simple view to render the home page
    """
    return render(request, 'googleMaps/home.html', {})


def get_images(request):
    """
        get_images(request)

        This view will determine if the images for Pasadena have 
        already been downloaded and saved as GMImage instances.  
        If so, we just need to pull them from the database and 
        render the html file to display them.  If not, we invoke 
        the appropriate function to download the images and save
        them to the database.
    """    
    # count how many GMimages are in the database, if there are none, call the get_pasadena_corner_images function
    if not GMImage.objects.all():
        the_images = get_pasadena_corner_images()
    # if there are images in the database, get the images from the database
    else:
        the_images = GMImage.objects.all()
    # use the get_pasadena_corner_images function to get the images, put them in the context dict
    context = {"GMImages": the_images}
    return render(request, 'googleMaps/get-images.html', context)


def refresh_images(request):
    """
        refresh_images(request)

        For demonstration purposes, this function will delete 
        all the images in the database and the redownload the 
        google map images for the 4 corners of Pasadena, CA by
        simpling calling the get_images function.
    """
    # delete all the images in the media/images directory
    for file in os.listdir(settings.IMAGES_ROOT):
        os.remove(os.path.join(settings.IMAGES_ROOT, file))
    # delete all the images in the database
    GMImage.objects.all().delete()
    # call the get_images function
    return get_images(request)
