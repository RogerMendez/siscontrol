# -*- coding: utf-8 -*-

from empleado.models import Empleado
from proveedor.models import Proveedor


from django.db import models

class Categoria(models.Model):
    cod_cat = models.CharField(max_length=50, unique=True, verbose_name='Codigo', null=True)
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s - %s' % (self.cod_cat, self.descripcion)
        #return '{} {}'.format(self.cod_cat, self.descripcion)
        #return self.descripcion

    def __str__(self):
        return '{} {}'.format(self.cod_cat, self.descripcion)
        #return '{}'.format(self.descripcion)

class Almacen(models.Model):
    cod_alm = models.CharField(max_length=50, unique=True, null=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        ordering = ['descripcion']

    def __unicode__(self):
        return self.descripcion

    def __str__(self):
        return self.descripcion

class Tipo_Medida(models.Model):
    descripcion = models.CharField(max_length=100)

    class Meta:
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion

class Articulo(models.Model):
    cod_art = models.CharField(max_length=50, unique=True, null=True)
    descripcion = models.CharField(max_length=100)
    marca = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=50, blank=True)
    stock_actual = models.PositiveIntegerField(verbose_name='Stock Actual', default='0')
    proveedor =  models.ForeignKey(Proveedor)
    categoria = models.ForeignKey(Categoria)
    almacen = models.ForeignKey(Almacen)
    medida = models.ForeignKey(Tipo_Medida)

    class Meta:
        permissions = (('ver_detalle_articulo', ' Can detail articulo'),)

    def __unicode__(self):
        return self.descripcion

    def __str__(self):
        return self.descripcion

class Ingreso(models.Model):
    articulo = models.ForeignKey(Articulo)
    empleado = models.ForeignKey(Empleado, verbose_name='Funcionario')
    cantidad = models.PositiveIntegerField()
    precio_u = models.FloatField()
    precio_t = models.FloatField()
    observacion = models.TextField(blank=True)
    fecha_i = models.DateTimeField(auto_now_add=True)
    #folio = models.IntegerField()
    factura = models.IntegerField(unique=True, verbose_name='N° de Factura')
    salida = models.IntegerField(null=True)
    saldo = models.IntegerField(null=True)
    total_i = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Ingresos'
        ordering = ['fecha_i']
        permissions = (('ver_detalle_ingreso', 'Can detail ingreso'),)

    def __str__(self):
        return self.articulo.descripcion


class Salida(models.Model):
    articulo = models.ForeignKey(Articulo, null=True)
    empleado = models.ForeignKey(Empleado, verbose_name='Funcionario')
    cantidad =  models.PositiveIntegerField()
    precio = models.FloatField(null=True)
    observacion = models.TextField(blank=True)
    fecha_s = models.DateTimeField(auto_now_add=True)
    total_s = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)


    class Meta:
        ordering = ['fecha_s']
        permissions = (('ver_detalle_salida', ' Can detail salida'),)

    def __str__(self):
        return self.articulo.descripcion