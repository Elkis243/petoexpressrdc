"""
URL configuration for congif project.

SEO (fichiers statiques) :
- /sitemap.xml — static/seo/sitemap.xml
- /robots.txt  — static/seo/robots.txt
"""
from django.contrib import admin
from django.urls import include, path

from core.seo_views import RobotsTxtView, SitemapXmlView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', SitemapXmlView.as_view(), name='sitemap_xml'),
    path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
    path('', include('core.urls')),
]
