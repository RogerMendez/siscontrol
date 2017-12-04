from django.db import models




genero = (('', 'Seleccione Genero'), ('Masculino','Masculino'), ('Femenino', 'Femenino'),)
class Proveedor(models.Model):
	ci = models.IntegerField(unique=True)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=100)
	genero = models.CharField(max_length=15, choices=genero)
	razon_social = models.CharField(max_length=150)
	direccion = models.CharField(max_length=150)
	telefono = models.CharField(max_length=15)
	correo = models.EmailField(blank=True)
	def __unicode__(self):
		return self.razon_social
	def __str__(self):
		return self.razon_social

	class Meta:
		permissions = (('ver_detalle_proveedor', 'Can detail proveedor'),)