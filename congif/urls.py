"""
URL configuration for congif project.

SEO:
- /sitemap.xml — pages publiques (core.sitemaps)
- /robots.txt — autorise le crawl public, bloque /admin/, pointe vers le sitemap
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from core.seo_views import RobotsTxtView
from core.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap',
    ),
    path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
    path('', include('core.urls')),
]
