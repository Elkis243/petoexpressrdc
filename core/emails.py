"""
Envoi d'e-mails du formulaire de contact (SMTP via settings / .env).
"""

from __future__ import annotations

import logging
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

logger = logging.getLogger("core.contact")


def send_contact_email(cleaned_data: dict) -> bool:
    """
    Envoie le message de contact à CONTACT_EMAIL_TO.
    Retourne True en cas de succès, False sinon (log sans secrets).
    """
    recipient = getattr(settings, "CONTACT_EMAIL_TO", None) or settings.DEFAULT_FROM_EMAIL
    if not recipient:
        logger.error("CONTACT_EMAIL_TO / DEFAULT_FROM_EMAIL non configuré.")
        return False

    sent_at = timezone.localtime(timezone.now())
    context = {
        **cleaned_data,
        "sent_at": sent_at,
        "site_name": "Peto Express SARL",
    }

    subject = f"[Contact] {_safe_subject(cleaned_data.get('subject', 'Nouvelle demande'))}"
    text_body = render_to_string("emails/contact_message.txt", context)
    html_body = render_to_string("emails/contact_message.html", context)

    from_email = settings.DEFAULT_FROM_EMAIL
    reply_to = [cleaned_data["email"]]

    try:
        message = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=from_email,
            to=[recipient],
            reply_to=reply_to,
        )
        message.attach_alternative(html_body, "text/html")
        message.send(fail_silently=False)
    except SMTPException:
        logger.exception(
            "Échec SMTP lors de l'envoi du formulaire de contact (destinataire=%s).",
            recipient,
        )
        return False
    except OSError:
        logger.exception(
            "Serveur SMTP inaccessible lors de l'envoi du formulaire de contact."
        )
        return False
    except Exception:
        logger.exception("Erreur inattendue lors de l'envoi du formulaire de contact.")
        return False

    logger.info(
        "Message de contact envoyé (from=%s, subject=%s).",
        cleaned_data.get("email"),
        cleaned_data.get("subject"),
    )
    return True


def _safe_subject(value: str) -> str:
    return " ".join(str(value).splitlines()).strip()[:180]
