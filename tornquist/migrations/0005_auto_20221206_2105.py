# Generated by Django 3.2.14 on 2022-12-07 00:05

from django.db import migrations, models
import tornquist.models


class Migration(migrations.Migration):

    dependencies = [
        ('tornquist', '0004_auto_20221206_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to='Actividades/'),
        ),
        migrations.AlterField(
            model_name='gastronomia',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to='Gastronomia/'),
        ),
        migrations.AlterField(
            model_name='puntosinteres',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to='PuntosInteres/'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to=tornquist.models.carpetas_de_guardado),
        ),
        migrations.AlterField(
            model_name='zonasalojamientos',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to='ZonasAlojamientos/'),
        ),
    ]