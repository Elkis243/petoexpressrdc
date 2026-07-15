# Peto Express SARL

Projet Peto Express SARL.

## E-mail / contact

Configuration SMTP uniquement via le fichier `.env` (`EMAIL_*`, `CONTACT_EMAIL_TO`).

```bash
# Variables dans .env (jamais committer ce fichier)
# Test local sans SMTP :
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

Le formulaire `/contact/` valide côté serveur, envoie un e-mail HTML+texte, affiche succès/erreur et journalise les échecs (`core.contact`).

`templates/base.html` inclut JSON-LD (`ProfessionalService` / `LocalBusiness`), canonical HTTPS, hreflang, geo, preloads LCP et métas OG/Twitter.

**Image sociale** : `static/images/social_network_logo.png` (1183×725). Idéal recommandé : **1200×630** — recadrer si besoin pour un rendu OG optimal.

| URL | Rôle |
|---|---|
| `/sitemap.xml` | Pages publiques (`core/sitemaps.py` → `PUBLIC_PAGES`) |
| `/robots.txt` | Autorise le crawl public, bloque `/admin/`, pointe vers le sitemap |

**Fichiers clés**
- `core/sitemaps.py` — ajouter chaque nouvelle page indexable dans `PUBLIC_PAGES`
- `core/seo_views.py` + `templates/robots.txt` — robots dynamique
- `congif/urls.py` — routes `/sitemap.xml` et `/robots.txt`

**Production (`www.petoexpressrdc.com`)**
```bash
export DJANGO_SETTINGS_MODULE=congif.settings.production
python manage.py migrate
python manage.py sync_site
```

URLs à soumettre dans Google Search Console :
- `https://www.petoexpressrdc.com/sitemap.xml`
- `https://www.petoexpressrdc.com/robots.txt`
