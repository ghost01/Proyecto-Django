from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Categoria(models.Model):
	nombre	= models.CharField(max_length = 100)
	descripcion	= models.TextField(max_length = 500)

	def __str__(self):
		return self.nombre

class Marca(models.Model):
	nombre	=models.CharField(max_length = 100)

	def __str__(self):
		return self.nombre

class Albumes(models.Model):
	nombre =models.CharField(max_length = 100)
	

	def __str__(self):
		return self.nombre


class Producto(models.Model):

	nombre	= models.CharField(max_length = 100)
	descripcion	= models.TextField(max_length = 500)
	imagen = models.ImageField(upload_to='musica', null = True, blank = True)
	status	= models.BooleanField(default = True)
	precio	= models.DecimalField(max_digits = 6, decimal_places = 2)
	stock	= models.IntegerField()
	categorias	= models.ManyToManyField(Categoria, null = True, blank = True)
	marca	= models.ForeignKey(Marca, on_delete = models.PROTECT)
	albumes = models.ForeignKey(Albumes, on_delete = models.CASCADE)

	def __str__(self):
		return self.nombre

class Replicas(models.Model):

	nombre =models.CharField(max_length = 100)
	descripcion = models.TextField(max_length = 100)
	productos = models.ManyToManyField(Producto, null = True, blank = True)

	def __str__(self):
		return self.nombre


class Perfil(models.Model):
	documento = models.CharField(max_length = 20)
	edad = models.IntegerField()
	telefono = models.CharField(max_length = 50)
	imagen = models.ImageField(upload_to='perfiles', null = True, blank = True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.documento

