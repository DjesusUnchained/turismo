from django.db import models

# Create your models here.

class CardABS(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre')
    ubicacion = models.CharField(max_length=150,verbose_name='ubicacion')
    telefono = models.CharField(max_length=150,verbose_name='telefono')
    direccion = models.CharField(max_length=150,verbose_name='direccion')
    pagina_web = models.CharField(max_length=150,verbose_name='pagina_web')
    url_img = models.ImageField(upload_to='imagenes/', max_length=200,verbose_name='url_img')

    class Meta:
        abstract = True


class Gastronomia(CardABS):
    pass
class Actividades(CardABS):
    pass
class PuntosInteres(CardABS):
    pass
class ZonasAlojamientos(CardABS):
    pass