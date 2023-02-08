"""
Django settings for base project.

Added settings for google maps api and file handling
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$3f2nj&e8erf=@ck2-7^9e^v=!j0=)-bz3z)y!pwq1796rh#z2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'googleMaps',
    'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / 'var/www/static/',
]

# set the media root and media url
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

# set the images root and images url
IMAGES_ROOT = MEDIA_ROOT / 'images'
IMAGES_URL = MEDIA_URL + 'images/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# google maps api settings
GOOGLE_MAPS_STATIC_API_URL = "https://maps.googleapis.com/maps/api/staticmap?"
API_KEY = "AIzaSyD-xIhMJKqVkL9vlb4KZxUnRqI7l9KZFUY"
API_SECRET = "68Xm8R7nmZ0BvFNhIhBBSIH4spo="
GOOGLE_MAPS_ZOOM_LEVEL = 20
GOOGLE_MAPS_SIZE_X = 1280
GOOGLE_MAPS_SIZE_Y = 1280
GOOGLE_MAPS_SCALE = 2
GOOGLE_MAPS_TYPE = "satellite"
GOOGLE_MAPS_FORMAT = "png"

# test location data from pasadena
PASADENA_CORNER_CORDS = {
    "coordinates": [
        {
            "NAME": "City of Pasadena - Top Left Corner",
            "LAT": 34.167424,
            "LONG": -118.186569
        },
        {
            "NAME": "City of Pasadena - Bottom Left Corner",
            "LAT": 34.141854,
            "LONG": -118.179875
        },
        {
            "NAME": "City of Pasadena - Top Right Corner",
            "LAT": 34.166572,
            "LONG": -118.088722
        },
        {
            "NAME": "City of Pasadena - Bottom Right Corner",
            "LAT": 34.144127,
            "LONG": -118.089924
        }
    ]
}

PASADENA_IMAGE_0 = "image_0"
PASADENA_IMAGE_1 = "image_1"
PASADENA_IMAGE_2 = "image_2"
PASADENA_IMAGE_3 = "image_3"

# image database settings
IMAGE_DB = "image_data.db"
IMAGE_DB_TABLE = "google_maps_images"
IMAGE_DB_PIXEL_TABLE = "pixels"
