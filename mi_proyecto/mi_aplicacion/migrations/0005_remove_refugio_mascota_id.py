# Generated by Django 5.0.6 on 2024-05-30 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0004_mascota_fecha_actualizacion_mascota_refugio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refugio',
            name='mascota_id',
        ),
    ]