"""
Sitemap public pages (django.contrib.sitemaps).

Ajouter une entrée dans PUBLIC_PAGES lorsqu'une nouvelle page
indexable est créée dans core.urls — le sitemap se met à jour seul.
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


# Pages publiques uniquement — admin / auth / erreurs exclus.
PUBLIC_PAGES = (
    {
        "name": "core:home",
        "priority": 1.0,
        "changefreq": "weekly",
    },
    {
        "name": "core:nettoyage_professionnel",
        "priority": 0.9,
        "changefreq": "monthly",
    },
    {
        "name": "core:entretien_et_traitement",
        "priority": 0.9,
        "changefreq": "monthly",
    },
    {
        "name": "core:hygiene_et_assainissement",
        "priority": 0.9,
        "changefreq": "monthly",
    },
    {
        "name": "core:secteurs_activite",
        "priority": 0.8,
        "changefreq": "monthly",
    },
    {
        "name": "core:a_propos",
        "priority": 0.7,
        "changefreq": "monthly",
    },
    {
        "name": "core:contact",
        "priority": 0.8,
        "changefreq": "monthly",
    },
)


class StaticViewSitemap(Sitemap):
    """Sitemap des vues statiques publiques (URL canoniques via reverse)."""

    protocol = "https"

    def items(self):
        return PUBLIC_PAGES

    def location(self, item):
        return reverse(item["name"])

    def priority(self, item):
        return item["priority"]

    def changefreq(self, item):
        return item["changefreq"]
