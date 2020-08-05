from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name="Nombre")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "categoria"
		verbose_name_plural = "categorias"
		ordering = ["-created"]

	def __str__(self):
		return self.name

class Product(models.Model):
	image = models.ImageField(verbose_name="Imagen")
	name = models.CharField(max_length=100, verbose_name="Nombre")
	description = models.TextField(max_length=500, verbose_name="Descripcion")
	price = models.FloatField(verbose_name="Precio")
	categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_product")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "producto"
		verbose_name_plural = "productos"
		ordering = ["-created"]

	def __str__(self):
		return self.name