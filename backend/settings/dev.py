"""
Development settings for fastresult_backend project.
Extends base settings with development-specific overrides.
"""
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Development tools
# (debug_toolbar requires additional configuration - optional for development)

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

# Email Backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database - SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# REST Framework Development Settings
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

# CORS - Allow all for development
CORS_ALLOW_ALL_ORIGINS = True

# Logging
LOGGING['loggers'] = {
    'django': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
}
