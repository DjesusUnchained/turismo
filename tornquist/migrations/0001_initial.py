# Generated by Django 3.2.14 on 2022-11-15 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('ubicacion', models.CharField(max_length=150, verbose_name='ubicacion')),
                ('telefono', models.CharField(max_length=150, verbose_name='telefono')),
                ('direccion', models.CharField(max_length=150, verbose_name='direccion')),
                ('pagina_web', models.CharField(max_length=150, verbose_name='pagina_web')),
                ('url_img', models.ImageField(max_length=200, upload_to='imagenes/', verbose_name='url_img')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gastronomia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('ubicacion', models.CharField(max_length=150, verbose_name='ubicacion')),
                ('telefono', models.CharField(max_length=150, verbose_name='telefono')),
                ('direccion', models.CharField(max_length=150, verbose_name='direccion')),
                ('pagina_web', models.CharField(max_length=150, verbose_name='pagina_web')),
                ('url_img', models.ImageField(max_length=200, upload_to='imagenes/', verbose_name='url_img')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PuntosInteres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('ubicacion', models.CharField(max_length=150, verbose_name='ubicacion')),
                ('telefono', models.CharField(max_length=150, verbose_name='telefono')),
                ('direccion', models.CharField(max_length=150, verbose_name='direccion')),
                ('pagina_web', models.CharField(max_length=150, verbose_name='pagina_web')),
                ('url_img', models.ImageField(max_length=200, upload_to='imagenes/', verbose_name='url_img')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ZonasAlojamientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('ubicacion', models.CharField(max_length=150, verbose_name='ubicacion')),
                ('telefono', models.CharField(max_length=150, verbose_name='telefono')),
                ('direccion', models.CharField(max_length=150, verbose_name='direccion')),
                ('pagina_web', models.CharField(max_length=150, verbose_name='pagina_web')),
                ('url_img', models.ImageField(max_length=200, upload_to='imagenes/', verbose_name='url_img')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
