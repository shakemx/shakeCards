from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

from base.models import BaseModel
from contact.models import Card
from tool.models import Utility


class User(BaseModel):
    name = models.CharField('Nombre', max_length=150, blank=False, null=False)
    photo = models.ImageField('Foto de Perfil', blank=False, null=False)
    cover = models.ImageField('Foto de Portada', blank=False, null=False)
    role = models.CharField('Puesto/Rol', max_length=50)
    bio = models.TextField('Biografía', max_length=500)
    tool = models.ManyToManyField(Utility, 'Utilerías', blank=True)
    contact = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name='Contacto')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home', kwargs={'slug': self.slug})