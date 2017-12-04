from django import template

register = template.Library()
from articulo.models import Ingreso, Salida

@register.simple_tag
def saldo_inicial(fecha):
    ingreso = Ingreso.objects.filter(fecha_i=fecha).first()
    return ingreso

@register.simple_tag
def inicial(num, num1):
    if num == num1:
        return True
    else:
        return False

@register.simple_tag
def ingreso(id):
    ingreso = Ingreso.objects.get(id = id)
    return ingreso

@register.simple_tag
def i_cantidad(id):
    ingreso = Ingreso.objects.get(id = id)
    return ingreso.cantidad

@register.simple_tag
def total():
    return 0

@register.simple_tag
def i_precio(id):
    ingreso = Ingreso.objects.get(id = id)
    return ingreso.precio_t

@register.simple_tag
def salida(id):
    ingreso = Salida.objects.get(id = id)
    return ingreso

@register.simple_tag
def sum_total(total, ingreso):
    return total + ingreso

@register.simple_tag
def sustractio_total(total, ingreso):
    return total - ingreso