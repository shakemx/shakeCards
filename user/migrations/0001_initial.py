# Generated by Django 4.2.1 on 2023-10-19 22:52

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tool', '0001_initial'),
        ('company', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('photo', models.ImageField(upload_to='', verbose_name='Foto de Perfil')),
                ('cover', models.ImageField(upload_to='', verbose_name='Foto de Portada')),
                ('role', models.CharField(max_length=50, verbose_name='Puesto/Rol')),
                ('bio', models.TextField(max_length=500, verbose_name='Biografía')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Contacto')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.card', verbose_name='Contacto')),
                ('tool', models.ManyToManyField(related_name='Utilerías', to='tool.utility')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
