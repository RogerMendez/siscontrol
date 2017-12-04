from django import template
register = template.Library()

from django.db.models import Sum
from articulo.models import Ingreso

@register.simple_tag
def cant_ingresos(articulo):
    ingresos = Ingreso.objects.filter(articulo=articulo)
    return ingresos.__len__()

@register.simple_tag
def sum_precio_salida(salida):
    q1 = salida.aggregate(Sum('precio'))
    sum = q1['precio__sum']
    if not sum:
        return 0.0
    return sum