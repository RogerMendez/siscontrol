from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
	url(r'^departamento/$', login_required(Lista_Departamento.as_view()), name="lista_departamento"),
	url(r'^crear/departamento/$', login_required(Crear_Departamento.as_view()), name="crear_departamento"),
	url(r'^modificar/departamento/(?P<pk>.+)/$', login_required(Modificar_Departamento.as_view()), name="modificar_departamento"),
	url(r'^eliminar/departamento/(?P<pk>.+)/$', login_required(Eliminar_Departamento.as_view()), name="eliminar_departamento"),

	url(r'^empleado/$', login_required(Lista_Empleado.as_view()), name="lista_empleado"),
	url(r'^crear/empleado/$', login_required(Crear_Empleado.as_view()), name="crear_empleado"),
	url(r'^modificar/empleado/(?P<pk>.+)/$', login_required(Modificar_Empleado.as_view()), name="modificar_empleado"),
	url(r'^eliminar/empleado/(?P<pk>.+)/$', login_required(Eliminar_Empleado.as_view()), name="eliminar_empleado"),
	url(r'^detalle/empleado/(?P<pk>.+)/$', login_required(Detalle_Empleado.as_view()), name="detalle_empleado"),
]