"""
Alignement SEO du domaine django.contrib.sites (sitemap canonique).

Après migrate, ou via la commande « sync_site », le Site (SITE_ID) prend
SITE_DOMAIN / SITE_NAME définis dans les settings / variables d'environnement.
"""

from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError


def sync_site_domain(**kwargs):
    """Met à jour le Site Django utilisé par le sitemap."""
    try:
        from django.contrib.sites.models import Site

        Site.objects.update_or_create(
            pk=settings.SITE_ID,
            defaults={
                "domain": settings.SITE_DOMAIN,
                "name": settings.SITE_NAME,
            },
        )
    except (OperationalError, ProgrammingError, ImportError):
        pass
