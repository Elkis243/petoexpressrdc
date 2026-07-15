from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        from django.db.models.signals import post_migrate

        from core.site_utils import sync_site_domain

        # Sans sender : s'exécute après chaque migrate (y compris sites).
        post_migrate.connect(sync_site_domain)
