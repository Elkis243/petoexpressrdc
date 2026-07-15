"""
Production settings.
"""

import os

from .base import *  # noqa: F403

DEBUG = os.getenv('DEBUG', 'False') == 'True'

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        'ALLOWED_HOSTS',
        'www.petoexpressrdc.com,petoexpressrdc.com',
    ).split(',')
    if host.strip()
]

# Domaine canonique du sitemap / robots (avec www).
SITE_DOMAIN = os.environ.get('SITE_DOMAIN', 'www.petoexpressrdc.com')
SITE_NAME = os.environ.get('SITE_NAME', 'Peto Express SARL')

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        'CSRF_TRUSTED_ORIGINS',
        'https://www.petoexpressrdc.com,https://petoexpressrdc.com',
    ).split(',')
    if origin.strip()
]
