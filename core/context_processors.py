"""
Context processor SEO — URLs canoniques HTTPS basées sur SITE_DOMAIN.
"""

from django.conf import settings


def seo(request):
    domain = getattr(settings, "SITE_DOMAIN", None) or request.get_host()
    # En local DEBUG, garder le schéma réel ; en prod forcer HTTPS.
    if settings.DEBUG:
        scheme = request.scheme or "http"
        # SITE_DOMAIN local peut déjà contenir le port (localhost:8000)
        origin = f"{scheme}://{domain}"
    else:
        scheme = "https"
        origin = f"{scheme}://{domain}"

    path = request.path or "/"
    return {
        "SEO_SITE_DOMAIN": domain,
        "SEO_SITE_NAME": getattr(settings, "SITE_NAME", "Peto Express SARL"),
        "SEO_ORIGIN": origin,
        "SEO_CANONICAL_URL": f"{origin}{path}",
        "SEO_LANG": "fr",
        "SEO_LOCALE": "fr_FR",
    }
