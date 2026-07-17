"""
Génération des fichiers SEO statiques (sitemap.xml, robots.txt).

Détecte automatiquement les routes nommées de core.urls et applique
les métadonnées définies dans PUBLIC_PAGES.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

from django.conf import settings
from django.urls import NoReverseMatch, reverse

SEO_DOMAIN = 'https://www.petoexpressrdc.com'

# Métadonnées par route publique (clé = "core:<url_name>").
PUBLIC_PAGES: dict[str, dict[str, str]] = {
    'core:home': {'priority': '1.0', 'changefreq': 'weekly'},
    'core:nettoyage_professionnel': {'priority': '0.9', 'changefreq': 'monthly'},
    'core:entretien_et_traitement': {'priority': '0.9', 'changefreq': 'monthly'},
    'core:hygiene_et_assainissement': {'priority': '0.9', 'changefreq': 'monthly'},
    'core:secteurs_activite': {'priority': '0.8', 'changefreq': 'monthly'},
    'core:a_propos': {'priority': '0.7', 'changefreq': 'monthly'},
    'core:contact': {'priority': '0.8', 'changefreq': 'monthly'},
}

DEFAULT_PAGE_META = {'priority': '0.5', 'changefreq': 'monthly'}

ROBOTS_DISALLOW_PATHS = (
    '/admin/',
)


def discover_public_route_names() -> list[str]:
    """Liste les routes nommées de core.urls (pages publiques du site)."""
    from core import urls as core_urls

    names: list[str] = []
    for pattern in core_urls.urlpatterns:
        if getattr(pattern, 'name', None):
            names.append(f'core:{pattern.name}')
    return names


def get_sitemap_entries() -> list[dict[str, str]]:
    """Construit les entrées du sitemap à partir des routes découvertes."""
    lastmod = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    entries: list[dict[str, str]] = []

    for route_name in discover_public_route_names():
        try:
            path = reverse(route_name)
        except NoReverseMatch:
            continue

        meta = PUBLIC_PAGES.get(route_name, DEFAULT_PAGE_META)
        entries.append(
            {
                'loc': f'{SEO_DOMAIN}{path}',
                'lastmod': lastmod,
                'changefreq': meta['changefreq'],
                'priority': meta['priority'],
            }
        )

    return entries


def build_sitemap_xml() -> str:
    """Retourne un sitemap XML conforme au protocole Google."""
    urlset = Element(
        'urlset',
        xmlns='http://www.sitemaps.org/schemas/sitemap/0.9',
    )

    for entry in get_sitemap_entries():
        url = SubElement(urlset, 'url')
        SubElement(url, 'loc').text = entry['loc']
        SubElement(url, 'lastmod').text = entry['lastmod']
        SubElement(url, 'changefreq').text = entry['changefreq']
        SubElement(url, 'priority').text = entry['priority']

    rough = tostring(urlset, encoding='unicode')
    return minidom.parseString(rough).toprettyxml(indent='  ', encoding=None).strip()


def build_robots_txt() -> str:
    """Retourne le contenu de robots.txt."""
    lines = [
        'User-agent: *',
        'Allow: /',
        '',
    ]
    for path in ROBOTS_DISALLOW_PATHS:
        lines.append(f'Disallow: {path}')
    lines.extend(
        [
            '',
            f'Sitemap: {SEO_DOMAIN}/sitemap.xml',
        ]
    )
    return '\n'.join(lines) + '\n'


def seo_static_dir() -> Path:
    return Path(settings.BASE_DIR) / 'static' / 'seo'


def write_seo_files() -> tuple[Path, Path]:
    """Écrit sitemap.xml et robots.txt dans static/seo/."""
    target_dir = seo_static_dir()
    target_dir.mkdir(parents=True, exist_ok=True)

    sitemap_path = target_dir / 'sitemap.xml'
    robots_path = target_dir / 'robots.txt'

    sitemap_path.write_text(build_sitemap_xml(), encoding='utf-8')
    robots_path.write_text(build_robots_txt(), encoding='utf-8')

    return sitemap_path, robots_path
