# Generated by Django 4.1.2 on 2022-12-05 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tornquist', '0008_alter_solicitud_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Actividades/'),
        ),
        migrations.AddField(
            model_name='puntosinteres',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Puntos de interes/'),
        ),
        migrations.AddField(
            model_name='zonasalojamientos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Alojamiento/'),
        ),
        migrations.AlterField(
            model_name='gastronomia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Gastronomia/'),
        ),
    ]