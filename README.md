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

**Image sociale** : `static/images/social_network_logo.webp`

| URL | Rôle |
|---|---|
| `/sitemap.xml` | Sitemap statique (`static/seo/sitemap.xml`) |
| `/robots.txt` | Robots statique (`static/seo/robots.txt`) |

**Fichiers clés**
- `core/seo_static.py` — routes publiques + génération XML/robots
- `core/seo_views.py` — sert les fichiers à la racine
- `python manage.py generate_seo_files` — régénère le sitemap après ajout de page

**Production (`www.petoexpressrdc.com`)**
```bash
export DJANGO_SETTINGS_MODULE=congif.settings.production
python manage.py migrate
python manage.py generate_seo_files
python manage.py collectstatic --noinput
```

URLs à soumettre dans Google Search Console :
- `https://www.petoexpressrdc.com/sitemap.xml`
- `https://www.petoexpressrdc.com/robots.txt`
