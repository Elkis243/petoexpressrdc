"""
Common Django settings for the congif project.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')

# SECURITY WARNING: don't run with debug turned on in production!
# Controlled exclusively by DJANGO_DEBUG in the environment / .env
# Local: DJANGO_DEBUG=True | Production (Railway): DJANGO_DEBUG=False
DEBUG = str(os.getenv('DJANGO_DEBUG', 'False')).strip().lower() in {
    '1',
    'true',
    'yes',
    'on',
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'core.apps.CoreConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'congif.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'core.context_processors.seo',
            ],
        },
    },
]

WSGI_APPLICATION = 'congif.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Africa/Kinshasa'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Email (variables d'environnement / .env — aussi sur Railway en prod)
EMAIL_BACKEND = os.getenv(
    'EMAIL_BACKEND',
    'django.core.mail.backends.smtp.EmailBackend',
)
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.hostinger.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT') or 587)
EMAIL_USE_TLS = str(os.getenv('EMAIL_USE_TLS', 'True')).strip().lower() in {
    '1',
    'true',
    'yes',
    'on',
}
EMAIL_USE_SSL = str(os.getenv('EMAIL_USE_SSL', 'False')).strip().lower() in {
    '1',
    'true',
    'yes',
    'on',
}
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
# Ne jamais laisser la valeur littérale "EMAIL_HOST_USER" dans .env
_default_from = os.getenv('DEFAULT_FROM_EMAIL', '').strip()
if not _default_from or _default_from == 'EMAIL_HOST_USER':
    _default_from = EMAIL_HOST_USER or 'noreply@localhost'
DEFAULT_FROM_EMAIL = _default_from
SERVER_EMAIL = DEFAULT_FROM_EMAIL
CONTACT_EMAIL_TO = os.getenv('CONTACT_EMAIL_TO', DEFAULT_FROM_EMAIL)
# Évite le hang gunicorn si le SMTP est injoignable (souvent le cas sur Railway)
EMAIL_TIMEOUT = int(os.getenv('EMAIL_TIMEOUT') or 15)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {name}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'core.contact': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

