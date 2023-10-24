from django.db import models

from base.models import BaseModel
from contact.models import Card
from service.models import Service
from tool.models import Utility


class Company(BaseModel):
    name = models.CharField('Nombre', max_length=50, blank=False, null=False)
    slogan = models.CharField('Slogan', max_length=50, blank=False, null=False)
    logo = models.ImageField('Logo - Compañia', blank=False, null=False)
    cover = models.ImageField('Portada - Compañia', blank=False, null=False)
    tool = models.ManyToManyField(Utility, 'Utilerias', )
    contact = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card')
    service = models.ManyToManyField(Service, verbose_name='Servicios')


    class Meta:
        verbose_name = 'Compania'
        verbose_name_plural = 'Companias'
    
    def __str__(self):
        return self.name

