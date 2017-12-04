from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from articulo import views


urlpatterns = [
    url(r'^categoria/$', Lista_Categoria.as_view(), name="lista_categoria"),
    url(r'^crear/categoria/$', Crear_Categoria.as_view(), name="crear_categoria"),
    url(r'^modificar/categoria/(?P<pk>\d+)/$', Modificar_Categoria.as_view(), name="modificar_categoria"),
    url(r'^eliminar/categoria/(?P<pk>\d+)/$', Eliminar_Categoria.as_view(), name="eliminar_categoria"),
    url(r'^pdf/categoria/$', Crear_Categoria_PDF, name="crear_categoria_pdf"),

    url(r'^lista/categoria/(?P<categoria_id>\d+)/$', Detalle_Categoria, name="detalle_categoria"),


    url(r'^almacen/$', Lista_Almacen.as_view(), name="lista_almacen"),
    #url(r'^crear/almacen/$', Crear_Almacen.as_view(), name="crear_almacen"),
    url(r'^crear/almacen/$', new_almacen, name="crear_almacen"),
    url(r'^modificar/almacen/(?P<pk>\d+)/$', Modificar_Almacen.as_view(), name="modificar_almacen"),
    url(r'^eliminar/almacen/(?P<pk>\d+)/$', Eliminar_Almacen.as_view(), name="eliminar_almacen"),

    url(r'^medida/$', Lista_Medida.as_view(), name="lista_medida"),
    url(r'^crear/medida/$', Crear_Medida.as_view(), name="crear_medida"),
    url(r'^modificar/medida/(?P<pk>\d+)/$', Modificar_Medida.as_view(), name="modificar_medida"),
    url(r'^eliminar/medida/(?P<pk>\d+)/$', Eliminar_Medida.as_view(), name="eliminar_medida"),

    url(r'^material/$', Lista_Articulo.as_view(), name="lista_articulo"),
    #url(r'^crear/material/$', Crear_Articulo.as_view(), name="crear_articulo"),
    url(r'^crear/material/$', views.new_articulo, name="crear_articulo"),

    url(r'^modificar/material/(?P<pk>\d+)/$', Modificar_Articulo.as_view(), name="modificar_articulo"),
    url(r'^eliminar/material/(?P<pk>\d+)/$', Eliminar_Articulo.as_view(), name="eliminar_articulo"),
    url(r'^detalle/material/(?P<pk>\d+)/$', Detalle_Articulo.as_view(), name="detalle_articulo"),

    url(r'^ingreso/$', Lista_Ingreso.as_view(), name="lista_ingreso"),
    url(r'^crear/ingreso/(?P<id_art>\d+)/$',Crear_Ingreso, name='crear_ingreso'),
    url(r'^detalle/ingreso/(?P<pk>\d+)/$', Detalle_Ingreso.as_view(), name="detalle_ingreso"),
    url(r'^kardex/ingreso/(?P<id_ing>\d+)/$', Crear_PDF_Ingreso, name='crear_pdf_ingreso'),
    url (r'ingresos/reporte/$', Crear_Reporte_Ingresos, name = 'crear_reporte_ingresos'),



    url(r'^salida/$', Lista_Salida.as_view(), name="lista_salida"),
    url(r'^crear/salida/(?P<id_articulo>\d+)/$',Crear_Salida, name='crear_salida'),
    url(r'^detalle/salida/(?P<pk>\d+)/$', Detalle_Salida.as_view(), name="detalle_salida"),
    url(r'^kardex/salida/(?P<id_sal>\d+)/$', Crear_PDF_Salida, name='crear_pdf_salida'),
    url (r'salidas/reporte/$', Crear_Reporte_Salidas, name = 'crear_reporte_salidas'),

    url(r'^error/stock/$', Error_Stock.as_view(), name="error_stock"),

    url(r'^kardex/(?P<articulo_id>\d+)/movimiento/$', views.kardex_movimientos , name="articulo-kardex-movimiento"),
    url(r'^pdf/(?P<articulo_id>\d+)/movimiento/$', views.Crear_PDF_Movimiento , name="crear_pdf_movimiento"),

]