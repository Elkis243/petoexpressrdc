"""
Context processor SEO — URLs canoniques basées sur la requête courante.
"""

from django.conf import settings


def seo(request):
    host = request.get_host()
    if settings.DEBUG:
        scheme = request.scheme or "http"
    else:
        scheme = "https"

    origin = f"{scheme}://{host}"
    path = request.path or "/"
    return {
        "SEO_ORIGIN": origin,
        "SEO_CANONICAL_URL": f"{origin}{path}",
        "SEO_LANG": "fr",
        "SEO_LOCALE": "fr_FR",
    }
