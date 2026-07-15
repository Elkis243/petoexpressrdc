"""
Formulaire de contact — validation serveur.
"""

import re

from django import forms
from django.core.exceptions import ValidationError


def _clean_header(value: str) -> str:
    """Supprime les retours de ligne pour éviter l'injection d'en-têtes e-mail."""
    return re.sub(r"[\r\n]+", " ", value).strip()


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nom",
        max_length=120,
        required=True,
        error_messages={
            "required": "Veuillez indiquer votre nom.",
            "max_length": "Le nom ne peut pas dépasser 120 caractères.",
        },
    )
    phone = forms.CharField(
        label="Téléphone",
        max_length=40,
        required=True,
        error_messages={
            "required": "Veuillez indiquer votre numéro de téléphone.",
            "max_length": "Le numéro ne peut pas dépasser 40 caractères.",
        },
    )
    email = forms.EmailField(
        label="Adresse e-mail",
        max_length=254,
        required=True,
        error_messages={
            "required": "Veuillez indiquer votre adresse e-mail.",
            "invalid": "Veuillez indiquer une adresse e-mail valide.",
            "max_length": "L'adresse e-mail est trop longue.",
        },
    )
    company = forms.CharField(
        label="Société / Organisation",
        max_length=150,
        required=False,
    )
    subject = forms.CharField(
        label="Sujet",
        max_length=200,
        required=True,
        error_messages={
            "required": "Veuillez indiquer le sujet de votre demande.",
            "max_length": "Le sujet ne peut pas dépasser 200 caractères.",
        },
    )
    message = forms.CharField(
        label="Message",
        max_length=5000,
        required=True,
        widget=forms.Textarea,
        error_messages={
            "required": "Veuillez écrire votre message.",
            "max_length": "Le message ne peut pas dépasser 5000 caractères.",
        },
    )

    def clean_name(self):
        return _clean_header(self.cleaned_data["name"])

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        if len(phone) < 6:
            raise ValidationError("Veuillez indiquer un numéro de téléphone valide.")
        return _clean_header(phone)

    def clean_email(self):
        return _clean_header(self.cleaned_data["email"].lower())

    def clean_company(self):
        company = self.cleaned_data.get("company") or ""
        return _clean_header(company)

    def clean_subject(self):
        return _clean_header(self.cleaned_data["subject"])

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise ValidationError("Votre message est trop court.")
        return message
