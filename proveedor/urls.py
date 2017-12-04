from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^proveedor/$', login_required(Lista_Proveedor.as_view()), name="lista_proveedor"),
    url(r'^crear/proveedor/$', login_required(Crear_Proveedor.as_view()), name="crear_proveedor"),
    url(r'^modificar/proveedor/(?P<pk>.+)/$', login_required(Modificar_Proveedor.as_view()), name="modificar_proveedor"),
    url(r'^detalle/proveedor/(?P<pk>.+)/$', login_required(Detalle_Proveedor.as_view()), name="detalle_proveedor"),
    url(r'^eliminar/proveedor/(?P<pk>.+)/$', login_required(Eliminar_Proveedor.as_view()), name="eliminar_proveedor"),
]