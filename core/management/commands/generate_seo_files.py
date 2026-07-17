"""
Génère static/seo/sitemap.xml et static/seo/robots.txt.

Usage:
  python manage.py generate_seo_files
"""

from django.core.management.base import BaseCommand

from core.seo_static import get_sitemap_entries, write_seo_files


class Command(BaseCommand):
    help = 'Génère les fichiers SEO statiques (sitemap.xml, robots.txt).'

    def handle(self, *args, **options):
        sitemap_path, robots_path = write_seo_files()
        entries = get_sitemap_entries()

        self.stdout.write(self.style.SUCCESS(f'Sitemap : {sitemap_path}'))
        self.stdout.write(self.style.SUCCESS(f'Robots  : {robots_path}'))
        self.stdout.write(f'{len(entries)} URL(s) publiques :')
        for entry in entries:
            self.stdout.write(f'  - {entry["loc"]}')
