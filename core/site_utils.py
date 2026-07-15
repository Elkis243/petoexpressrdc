"""
Alignement SEO du domaine django.contrib.sites (sitemap canonique).
"""

from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError


def sync_site_domain(**kwargs):
    """Met à jour le Site Django utilisé par le sitemap."""
    try:
        from django.contrib.sites.models import Site

        domain = (
            "localhost:8000" if settings.DEBUG else "www.petoexpressrdc.com"
        )
        Site.objects.update_or_create(
            pk=settings.SITE_ID,
            defaults={
                "domain": domain,
                "name": "Peto Express SARL",
            },
        )
    except (OperationalError, ProgrammingError, ImportError):
        pass
