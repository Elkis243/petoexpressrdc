"""
Production settings.
"""

import os

from .base import *  # noqa: F403

DEBUG = os.getenv('DEBUG', 'False') == 'True'

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get('ALLOWED_HOSTS', '').split(',')
    if host.strip()
]
