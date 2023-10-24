from django.urls import path

from web.views import home, card


urlpatterns = [
    path('', home, name='home'), 
    path('<slug:slug>', card, name='card')
]