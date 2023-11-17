from colorfield.fields import ColorField

from django.db import models
from base.models import BaseModel

class ColorCompany(BaseModel):
    template = models.CharField('Template',  max_length=50, blank=False, null=False)
    description = models.CharField('Descripción', max_length=100)
    bg_main = ColorField('Fondo',format="hexa",default='#fffffe')
    text_main = ColorField('Texto Principal',format="hexa",default='#2b2c34')
    text_secondary = ColorField('Texto Secundario',format="hexa",default='#fffffe')
    company_main = ColorField('Empresa',format="hexa",default='#6246ea')
    company_secondary = ColorField('Empresa Secundario',format="hexa",default='#d1d1e9')
    company_icon = ColorField('Icono Empresa',format="hexa",default='#fffffe')
    icono_main = ColorField('Icono Principal',format="hexa",default='#6246ea')
    icono_secondary = ColorField('Icono Secundario',format="hexa",default='#6246ea')
    class Meta:
        verbose_name = 'Tema de Empresa'
        verbose_name_plural = 'Temas de Empresa'
    
    def __str__(self):
        return self.template 
    