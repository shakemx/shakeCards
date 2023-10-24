from django.db import models

from base.models import BaseModel


class Card(BaseModel):
    USER = 'USER'
    COMPANY = 'COMPANY'
    CHOICE_TYPE =[
        (USER, 'Usuario'),
        (COMPANY, 'Empresa'),
    ]
    name = models.CharField('Nombre', max_length=50, blank=False, null=False)
    mail = models.EmailField('Correo')
    phone = models.CharField('Teléfono', max_length=15, blank=True,)
    mobile = models.CharField('Celular', max_length=15, blank=False, null=False)
    whatsapp = models.CharField('Whatsapp Business', max_length=15, blank=False, null=False)
    web = models.URLField('Sitio Web',blank=True,)
    schedule = models.CharField('Horario', max_length=100, blank=True,)
    type = models.CharField('Tipo', max_length=10, choices=CHOICE_TYPE, default=USER, blank=False)


    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return self.name
