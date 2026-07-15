"""
Development settings.
"""

import os

from .base import *  # noqa: F403

DEBUG = os.getenv('DEBUG', 'True') == 'True'

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-jv4zmpmiz+z978^j9v_---h&*62&*sx9ff9%rd$cdmqo#26_ad',
)

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
    if host.strip()
]

SITE_DOMAIN = os.getenv('SITE_DOMAIN', 'localhost:8000')
SITE_NAME = os.getenv('SITE_NAME', 'Peto Express SARL')

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        'CSRF_TRUSTED_ORIGINS',
        'http://localhost:8000,http://127.0.0.1:8000',
    ).split(',')
    if origin.strip()
]
