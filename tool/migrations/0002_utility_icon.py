# Generated by Django 4.2.1 on 2023-11-20 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colorTemplate', '0002_icon'),
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='colorTemplate.icon'),
        ),
    ]
