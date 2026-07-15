import os

import dj_database_url

from .base import *

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = [
    "petoexpressrdc-production.up.railway.app",
    "petoexpressrdc.com",
    "www.petoexpressrdc.com",
]

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,
    )
}

SECURE_HSTS_SECONDS = int(os.getenv('SECURE_HSTS_SECONDS', '31536000'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = (os.getenv('SECURE_HSTS_INCLUDE_SUBDOMAINS', 'True') == 'True')
SECURE_HSTS_PRELOAD = os.getenv('SECURE_HSTS_PRELOAD', 'True') == 'True'
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'True') == 'True'

SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'True') == 'True'
CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', 'True') == 'True'

CSRF_TRUSTED_ORIGINS = [
    "https://*.up.railway.app",
    "https://petoexpressrdc.com",
    "https://www.petoexpressrdc.com",
]

X_FRAME_OPTIONS = os.getenv('X_FRAME_OPTIONS', 'DENY')
SECURE_BROWSER_XSS_FILTER = (
    os.getenv('SECURE_BROWSER_XSS_FILTER', 'True') == 'True'
)
SECURE_CONTENT_TYPE_NOSNIFF = (
    os.getenv('SECURE_CONTENT_TYPE_NOSNIFF', 'True') == 'True'
)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Fichiers statiques (collectstatic → BASE_DIR/staticfiles)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise : servir les static files derrière gunicorn (juste après SecurityMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *[m for m in MIDDLEWARE if m != 'django.middleware.security.SecurityMiddleware'],
]

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
