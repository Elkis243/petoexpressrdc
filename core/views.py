from django.contrib import messages
from django.shortcuts import redirect, render

from .emails import send_contact_email
from .forms import ContactForm


def home(request):
    return render(
        request,
        'core/home.html',
        {
            'page': 'Home',
        },
    )


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if send_contact_email(form.cleaned_data):
                messages.success(
                    request,
                    "Votre message a été envoyé avec succès. "
                    "Notre équipe vous répondra dans les meilleurs délais.",
                )
                return redirect('core:contact')

            messages.error(
                request,
                "Une erreur est survenue lors de l'envoi de votre message. "
                "Veuillez réessayer ultérieurement.",
            )
        else:
            messages.error(
                request,
                "Veuillez corriger les champs indiqués avant de renvoyer le formulaire.",
            )

    return render(
        request,
        'core/contact.html',
        {
            'page': 'Contact',
            'form': form,
        },
    )


def nettoyage_professionnel(request):
    return render(
        request,
        'core/nettoyage_professionnel.html',
        {
            'page': 'Nettoyage professionnel',
        },
    )


def entretien_et_traitement(request):
    return render(
        request,
        'core/entretien_et_traitement.html',
        {
            'page': 'Entretien et traitement',
        },
    )


def hygiene_et_assainissement(request):
    return render(
        request,
        'core/hygiene_et_assainissement.html',
        {
            'page': 'Hygiène et assainissement',
        },
    )


def secteurs_activite(request):
    return render(
        request,
        'core/secteurs_activite.html',
        {
            'page': "Nos secteurs d'activité",
        },
    )


def a_propos(request):
    return render(
        request,
        'core/a_propos.html',
        {
            'page': 'À propos',
        },
    )
