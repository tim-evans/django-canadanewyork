from .common import *


#########
# TESTING #
#########
# must come after 'south', so that this version of `./manage.py test` takes precedence
INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-specplugin',
    '--detailed-errors',
    '--nologcapture',
    'tests'
]

########
# CACHE #
########

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
