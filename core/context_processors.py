"""
Context processor SEO — URLs canoniques.
"""

from django.conf import settings


def seo(request):
    if settings.DEBUG:
        scheme = request.scheme or 'http'
        origin = f'{scheme}://{request.get_host()}'
    else:
        origin = settings.SEO_SITE_URL

    path = request.path or '/'
    return {
        'SEO_ORIGIN': origin,
        'SEO_CANONICAL_URL': f'{origin}{path}',
        'SEO_SITEMAP_URL': f'{settings.SEO_SITE_URL}/sitemap.xml',
        'SEO_LANG': 'fr',
        'SEO_LOCALE': 'fr_FR',
    }
