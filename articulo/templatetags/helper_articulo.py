from django import template
register = template.Library()
#from articulo.models import Ingreso, Salida


@register.simple_tag
def suma(num1, num2):
    return num1 + num2

