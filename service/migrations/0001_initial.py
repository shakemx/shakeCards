# Generated by Django 4.2.1 on 2023-11-18 02:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('decription', models.TextField(max_length=500, verbose_name='Descripción')),
                ('logo', models.ImageField(blank=True, upload_to='', verbose_name='Logo - Servicio')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
