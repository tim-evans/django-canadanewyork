from os import path

from django.conf.global_settings import *

from canada.functions import add_to_middleware
import canada


SITE_ROOT = path.dirname(path.realpath(canada.__file__))

########
#CANADA
########
CANADA_IMAGE_SIZE = 'x300'
CANADA_FRONTPAGE_IMAGE_SIZE = 'x400'
CANADA_ADMIN_THUMBS_SIZE = 'x60'



INSTALLED_APPS = (
    'canada.apps.artists',
    'canada.apps.exhibitions',
    'canada.apps.press',
    'canada.apps.updates',
    'canada.apps.bulkmail',
    'canada.apps.updates',
    'canada.apps.frontpage',
  )

TEMPLATE_CONTEXT_PROCESSORS += ('canada.context_processors.image_size',)

########
#External Packages
########
INSTALLED_APPS += (
    'south',
    'grappelli',
    'sorl.thumbnail',
    'smart_selects'
  )

GRAPPELLI_ADMIN_TITLE = 'CANADA'


########
#Email
########
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "saul.shanabrook@gmail.com"
EMAIL_HOST_PASSWORD = "3j}s^52G-qH69%kY"
EMAIL_USE_TLS = True


########
#Django
########
DEBUG = False

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.markup',
  )

#Static/Media
STATICFILES_DIRS = (
    ('canada', path.join(SITE_ROOT, 'static')),
  )

MEDIA_URL = '/media/'
MEDIA_ROOT = path.normpath(path.join(SITE_ROOT, '../media/'))

STATIC_URL = '/static/'
STATIC_ROOT = path.normpath(path.join(SITE_ROOT, '../static/'))

FIXTURE_DIRS = (path.join(SITE_ROOT, 'fixtures'),)

#Admin
LOGIN_URL = '/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
ADMINS = (
    ('Saul Shanabrook', 'saul.shanabrook@gmail.com'),
  )


#Urls
ROOT_URLCONF = 'canada.urls'

#Templates
TEMPLATE_DIRS = (
    path.join(SITE_ROOT, 'templates'),
  )

MIDDLEWARE_CLASSES = add_to_middleware(MIDDLEWARE_CLASSES,
                                       'django.middleware.gzip.GZipMiddleware',
                                       prepend=True)
DATE_FORMAT = 'F j, Y'

########
#Security
########
SECURE_FRAME_DENY = True
SECRET_KEY = '*itk&52%kmo)f0+ase$uvsy6cmz04c@xr#7$n+bn7_=3wv0lz4'

TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.csrf',)