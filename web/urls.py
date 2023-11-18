from django.urls import path

from web.views import home, card, vcard, company


urlpatterns = [
    path('', home, name='home'), 
    path('<slug:slug>', company, name='company'),
    path('agente/<slug:slug>', card, name='card'),
    path('vcard/<slug:slug>', vcard, name='vcard')
]