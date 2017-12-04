from django.conf.urls import url
from reportes import views

urlpatterns = [
    url(r'^ingresos/$', views.report_ingreso, name="report-ingresos"),
    url(r'^detail/(?P<articulo_id>\d+)/$', views.detalle_ingreso, name="report-detail-ingresos"),
    url(r'^detail/(?P<articulo_id>\d+)/fechas/$', views.detalle_ingreso_fechas, name="report-detail-ingresos-fechas"),

    url(r'^pdf/detail/(?P<articulo_id>\d+)/$', views.pdf_detalle_ingreso, name="pdf-detail-ingresos"),
    url(r'^pdf/detail/(?P<articulo_id>\d+)/fechas/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/fecha/(?P<year1>\d+)/(?P<month1>\d+)/(?P<day1>\d+)$', views.pdf_detalle_ingreso_fechas, name="pdf-detail-ingresos-fechas"),


    url(r'^salidas/$', views.report_salida, name="report-salidas"),
    url(r'^detail/(?P<articulo_id>\d+)/salida/$', views.detalle_salidas, name="report-detail-salida"),
    url(r'^detail/(?P<articulo_id>\d+)/fechas/salida/$', views.detalle_salida_fechas, name="report-detail-salidas-fechas"),

    url(r'^pdf/detail/(?P<articulo_id>\d+)/salida/$', views.pdf_detalle_salida, name="pdf-detail-salida"),
    url(r'^pdf/detail/(?P<articulo_id>\d+)/salida/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/fecha/(?P<year1>\d+)/(?P<month1>\d+)/(?P<day1>\d+)$', views.pdf_detalle_salida_fechas, name="pdf-detail-salidas-fechas"),
]