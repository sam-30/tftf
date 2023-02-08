from googlemaps import Client
from base import settings
import errno, os, sys
from django.db import models
from googleMaps import models as gmm
import uuid

""" Utility functions to help with downloading images from google maps """

def convertPathToImageField(path) -> models.ImageField:
    """ 
        
        Converts an os path from a file system to a Django image field.  Used to prep 
        Google maps images to be used in saving a model to the database.  See the 
        save() function in models.py for the GMImage model.  The path parameter
        can be a string or an os.path object.  If it is a string, it will be converted

    """
    the_path = None

    # check if the path is an os.path or a string
    if isinstance(path, type(os.path)):
        the_path = path
    elif isinstance(path, str):
        the_path = os.path.realpath(path)
    else:
        return None

    # create a new GMImage model
    tempGMModel = gmm.GMImage()
    # get just the file name from the path
    file_name = os.path.basename(the_path)
    # set the image field to the file name relative to the media root directory
    tempGMModel.image.name = 'images/' + file_name

    return tempGMModel.image


def convertIterToImageField(the_iterable, file_path, file_name) -> models.ImageField:
    """ 
        Converts an iterable that the google maps static_map function returns to get chunks of
        the image and saves it to a file.  We then use the convertPathToImageField function using
        the path saved in this function.  The iterable parameter is the object returned from the
        google maps stati_map function.  The file path parameter should not have the file name included
        
    """
    try:
        with open(os.path.join(file_path, file_name + '.' + settings.GOOGLE_MAPS_FORMAT), 'wb') as f:
            for chunk in the_iterable:
                if chunk:
                    f.write(chunk)
            f.close()

        return convertPathToImageField(os.path.join(file_path, file_name + '.' + settings.GOOGLE_MAPS_FORMAT))
    except:
        return None

# error code for windows file not found error used in the is_pathname_valid function
ERROR_INVALID_NAME = 123

def is_pathname_valid(pathname: str) -> bool:
    '''
    This function validates a path to a folder.  We are checking for validity of the path
    not the existence of the folder.  This function was found in the following stack overflow:
    https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta

    `True` if the passed pathname is a valid pathname for the current OS;
    `False` otherwise.
    '''
    # If this pathname is either not a string or is but is empty, this pathname
    # is invalid.
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
        # if any. Since Windows prohibits path components from containing `:`
        # characters, failing to strip this `:`-suffixed prefix would
        # erroneously invalidate all valid absolute Windows pathnames.
        _, pathname = os.path.splitdrive(pathname)

        # Directory guaranteed to exist. If the current OS is Windows, this is
        # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
        # environment variable); else, the typical root directory.
        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname) 

        # Append a path separator to this directory if needed.
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        # Test whether each path component split from this pathname is valid or
        # not, ignoring non-existent and non-readable path components.
        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            # If an OS-specific exception is raised, its error code
            # indicates whether this pathname is valid or not. Unless this
            # is the case, this exception implies an ignorable kernel or
            # filesystem complaint (e.g., path not found or inaccessible).
            #
            # Only the following exceptions indicate invalid pathnames:
            #
            # * Instances of the Windows-specific "WindowsError" class
            #   defining the "winerror" attribute whose value is
            #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
            #   fine-grained and hence useful than the generic "errno"
            #   attribute. When a too-long pathname is passed, for example,
            #   "errno" is "ENOENT" (i.e., no such file or directory) rather
            #   than "ENAMETOOLONG" (i.e., file name too long).
            # * Instances of the cross-platform "OSError" class defining the
            #   generic "errno" attribute whose value is either:
            #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
            #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    # If a "TypeError" exception was raised, it almost certainly has the
    # error message "embedded NUL character" indicating an invalid pathname.
    except TypeError as exc:
        return False
    # If no exception was raised, all path components and hence this
    # pathname itself are valid. (Praise be to the curmudgeonly python.)
    else:
        return True


def download_image(lat, lon, file_path, file_name, gmap_client=None) -> models.ImageField:
    """
        
        Downloads an image from google maps using the latitude and longitude passed in.  
        The file path should not have the file name included.  Use the settings file to
        get magic numbers for the image size, format, zoom, type and scale. The Client
        is from the googlemaps library which is listed in the requirements.txt file.  
        This library provides a clean abstraction for the google maps api. 
        
    """    
    try:
        imageField = None

        # if the gmap_client is None, get a new client using the API key in the settings
        if gmap_client is None:
            gmaps = Client(key=settings.API_KEY)
        else:
            gmaps = gmap_client

        # download the image from google maps and pass the return value to the convertIterToImageField function to save the download to a file
        imageField = convertIterToImageField(the_iterable=gmaps.static_map(center=(lat, lon),
                                zoom=settings.GOOGLE_MAPS_ZOOM_LEVEL,
                                size=(settings.GOOGLE_MAPS_SIZE_X, settings.GOOGLE_MAPS_SIZE_Y),
                                maptype=settings.GOOGLE_MAPS_TYPE,
                                scale=settings.GOOGLE_MAPS_SCALE), file_path=file_path, file_name=file_name)
        
        return imageField
    except Exception as e:
        return None


def get_next_image_name():
    """ 
        Use this function to control the naming of the images downloaded from google maps.
        We want to use a function so that the naming convention can change.  For now we are
        assigning a random uuid to the image name. 
    """
    # create a random image name
    image_name = str(uuid.uuid4())
    return image_name