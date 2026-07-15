from django.shortcuts import render


def home(request):
    return render(
        request,
        'core/home.html',
        {
            'page': 'Home',
        },
    )


def contact(request):
    return render(
        request,
        'core/contact.html',
        {
            'page': 'Contact',
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
