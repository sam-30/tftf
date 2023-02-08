# tftf
TreesFromTheForrest Django Project - Code Sample

Install Django and pip in all required libraries.  API will work but is limited in how many times it can be queried.  Always use a virtual environment for safety's sake

Files of interest:

base/googleMaps/urls.py - manages the url pathing

base/googleMaps/models.py - contains the GMImage model representing a google maps image in the database

base/utils.py - a utility file that abstracts the image downloading away from the model

base/base/settings.py - the settings file that contains predetermined values, such as the API key, the coordinates of images we want to download, and more

base/templates/googleMaps/get-images.html - display file that shows the google maps images the program downloads
