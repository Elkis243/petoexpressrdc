"""
Vues SEO : sert les fichiers statiques sitemap.xml et robots.txt à la racine.
"""

from __future__ import annotations

from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404
from django.views import View

from core.seo_static import seo_static_dir, write_seo_files


def _ensure_seo_file(filename: str) -> Path:
    path = seo_static_dir() / filename
    if not path.is_file():
        write_seo_files()
    if not path.is_file():
        raise Http404(f'Fichier SEO introuvable : {filename}')
    return path


class SitemapXmlView(View):
    """Sert /sitemap.xml depuis static/seo/sitemap.xml."""

    def get(self, request, *args, **kwargs):
        path = _ensure_seo_file('sitemap.xml')
        return FileResponse(
            path.open('rb'),
            content_type='application/xml',
            headers={'Cache-Control': 'public, max-age=3600'},
        )


class RobotsTxtView(View):
    """Sert /robots.txt depuis static/seo/robots.txt."""

    def get(self, request, *args, **kwargs):
        path = _ensure_seo_file('robots.txt')
        return FileResponse(
            path.open('rb'),
            content_type='text/plain; charset=utf-8',
            headers={'Cache-Control': 'public, max-age=3600'},
        )
