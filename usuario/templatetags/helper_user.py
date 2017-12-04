from django import template
register = template.Library()

from usuario.models import Perfil

@register.simple_tag
def perfil(user_id):
	perfil = Perfil.objects.get(user_id = user_id)
	return perfil.photo