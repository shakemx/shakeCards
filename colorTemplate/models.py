from colorfield.fields import ColorField

from django.db import models
from base.models import BaseModel

class ColorCompany(BaseModel):
    template = models.CharField('Template',  max_length=50, blank=False, null=False)
    description = models.CharField('Descripción', max_length=100)
    bg_main = ColorField('Fondo',format="hexa",default='#fffffe', null=True)
    text_main = ColorField('Texto Principal',format="hexa",default='#2b2c34', null=True)
    text_secondary = ColorField('Texto Secundario',format="hexa",default='#fffffe', null=True)
    company_main = ColorField('Empresa',format="hexa",default='#6246ea', null=True)
    company_secondary = ColorField('Empresa Secundario',format="hexa",default='#d1d1e9', null=True)
    company_icon = ColorField('Icono Empresa',format="hexa",default='#fffffe', null=True)
    icono_main = ColorField('Icono Principal',format="hexa",default='#2B2C34', null=True)
    icono_secondary = ColorField('Icono Secundario',format="hexa",default='#6246ea', null=True)
    icono_services = ColorField('Icono Servicios',format="hexa",default='#6246ea',null=True)
    icono_utilities = ColorField('Icono Utilerias',format="hexa",default='#fffffe',null=True)
    class Meta:
        verbose_name = 'Tema de Empresa'
        verbose_name_plural = 'Temas de Empresa'
    
    def __str__(self):
        return self.template 
    

class Icon(BaseModel):
    name = models.CharField('Nombre', max_length=50, blank=False, null=False)
    icon = models.CharField('Icono', max_length=50, blank=False, null=False)
    class Meta:
        verbose_name = 'Icono'
        verbose_name_plural = 'Iconos'

    def __str__(self):
        return self.name

    