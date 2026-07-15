from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path(
        'services/nettoyage-professionnel/',
        views.nettoyage_professionnel,
        name='nettoyage_professionnel',
    ),
    path(
        'services/entretien-et-traitement/',
        views.entretien_et_traitement,
        name='entretien_et_traitement',
    ),
    path(
        'services/hygiene-et-assainissement/',
        views.hygiene_et_assainissement,
        name='hygiene_et_assainissement',
    ),
    path(
        'secteurs-activite/',
        views.secteurs_activite,
        name='secteurs_activite',
    ),
    path('a-propos/', views.a_propos, name='a_propos'),
]
