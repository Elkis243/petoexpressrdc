# Peto Express RDC

Projet Peto Express RDC.

## SEO (sitemap & robots)

| URL | Rôle |
|---|---|
| `/sitemap.xml` | Pages publiques (`core/sitemaps.py` → `PUBLIC_PAGES`) |
| `/robots.txt` | Autorise le crawl public, bloque `/admin/`, pointe vers le sitemap |

**Fichiers clés**
- `core/sitemaps.py` — ajouter chaque nouvelle page indexable dans `PUBLIC_PAGES`
- `core/seo_views.py` + `templates/robots.txt` — robots dynamique
- `congif/urls.py` — routes `/sitemap.xml` et `/robots.txt`
- `SITE_DOMAIN` / `SITE_NAME` (env) — domaine canonique du sitemap (framework Sites)

**Production (`www.petoexpressrdc.com`)**
```bash
export DJANGO_SETTINGS_MODULE=congif.settings.production
export SITE_DOMAIN=www.petoexpressrdc.com
python manage.py migrate
python manage.py sync_site
```

URLs à soumettre dans Google Search Console :
- `https://www.petoexpressrdc.com/sitemap.xml`
- `https://www.petoexpressrdc.com/robots.txt`
