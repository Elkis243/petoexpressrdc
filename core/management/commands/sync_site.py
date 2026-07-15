"""
Met à jour le domaine Site pour le sitemap.

Usage:
  python manage.py sync_site
"""

from django.core.management.base import BaseCommand

from core.site_utils import sync_site_domain


class Command(BaseCommand):
    help = "Synchronise django.contrib.sites (domaine local ou www.petoexpressrdc.com)."

    def handle(self, *args, **options):
        sync_site_domain()
        from django.conf import settings
        from django.contrib.sites.models import Site

        site = Site.objects.get(pk=settings.SITE_ID)
        self.stdout.write(
            self.style.SUCCESS(
                f"Site #{site.pk} → domain={site.domain!r}, name={site.name!r}"
            )
        )
