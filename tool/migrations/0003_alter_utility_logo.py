# Generated by Django 4.2.1 on 2023-11-20 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_utility_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utility',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Logo - Icon'),
        ),
    ]
