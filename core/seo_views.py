"""
SEO views: robots.txt dynamique (référence le sitemap du même hôte).
"""

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.views.generic import TemplateView


class RobotsTxtView(TemplateView):
    """Sert /robots.txt en text/plain avec l'URL absolue du sitemap."""

    template_name = "robots.txt"
    content_type = "text/plain"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site = get_current_site(self.request)
        sitemap_path = reverse("django.contrib.sitemaps.views.sitemap")
        # Aligné sur le protocole https du sitemap (URL canonique).
        context["sitemap_url"] = f"https://{site.domain}{sitemap_path}"
        if settings.DEBUG and "localhost" in site.domain:
            # En local, refléter le schéma HTTP réel pour les tests.
            context["sitemap_url"] = self.request.build_absolute_uri(sitemap_path)
        return context
