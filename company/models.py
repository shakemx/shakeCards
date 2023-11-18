from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

from base.models import BaseModel
from colorTemplate.models import ColorCompany
from contact.models import Card
from service.models import Service
from tool.models import Utility
from user.models import User


class Company(BaseModel):
    name = models.CharField('Nombre', max_length=50, blank=False, null=False)
    slogan = models.CharField('Slogan', max_length=50, blank=False, null=False)
    logo = models.ImageField('Logo - Compañia', blank=False, null=False)
    color = models.ForeignKey(ColorCompany, on_delete=models.CASCADE, verbose_name='Tema',blank=True, null=True)
    cover = models.ImageField('Portada - Compañia', blank=False, null=False)
    tool = models.ManyToManyField(Utility, 'Utilerias', )
    contact = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card')
    service = models.ManyToManyField(Service, verbose_name='Servicios')
    user = models.ManyToManyField(User, verbose_name='Usuarios')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=False)


    class Meta:
        verbose_name = 'Compania'
        verbose_name_plural = 'Companias'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home', kwargs={'slug': self.slug})

