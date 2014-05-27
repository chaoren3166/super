__author__ = 'weichao02'
import os
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'super',
        'USER': 'chaoren',
        'PASSWORD': 'chaoren',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

PARENT_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir
))

LOG_PATH = os.path.join(PARENT_PATH + '/logs/')