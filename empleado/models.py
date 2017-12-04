from django.db import models
from django.core.exceptions import ValidationError
#from almacen.apps.material.models import Ingreso, Salida

class Departamento (models.Model):
    descripcion = models.CharField(max_length=50, verbose_name='Nombre de Unidad')
    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
        ordering = ['descripcion']
    def __str__(self):
        return self.descripcion
    def __unicode__(self):
        return self.descripcion


CARGO  = (
			('', 'Selecione    Cargo '),
			('Auditor (a)', 'Auditor (a)'),
			('Cotizador (a)', 'Cotizador (a)'),
			('Contador (a)', 'Contador (a)'),
			('Enc. Almacenes', 'Enc. Almacenes'),
			('Enc. Area Tecnica', 'Enc. Area Tecnica'),
			('Enc. Bienes', 'Enc. Bienes'),
			('Enc. R. Humanos ', 'Enc. R. Humanos '),
			('Enc. Tesoreria', 'Enc. Tesoreria'),
			('Enc. Soldaduria', 'Enc. Soldaduria'),
			('Gerente General', 'Gerente General'),
			('Ing. de Sistemas', 'Ing. de Sistemas'),
			('Mecanico', 'Mecanico'),
			('Resp. Archivos', 'Resp. Archivos'),
			('Secretaria', 'Secretaria'),
			('Supervisor', 'Supervisor'),
		)

def validate_ci(value):
    if len(str(value)) != 8 and len(str(value)) != 7:
        raise ValidationError(u'%s No es un Cedula de Identidad'% value)
    return validate_ci

class Empleado (models.Model):
    ci = models.PositiveIntegerField(validators=[validate_ci], unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cargo = models.CharField(choices = CARGO, max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    departamento = models.ForeignKey(Departamento)
    def __unicode__(self):
        return '%s %s' % (self.nombre, self.apellidos)
    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)
    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
        ordering = ['id']

        permissions = (('ver_detalle_empleado', 'Can detail empleado'),)