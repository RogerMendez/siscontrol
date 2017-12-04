# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from io import BytesIO
from django.template.loader import get_template, render_to_string
from django.template import RequestContext
from django.core.urlresolvers import reverse
#import xhtml2pdf.pisa as pisa
from django import http

import ho.pisa as pisa
import cStringIO as StringIO
import cgi
#from articulo.utils import render_to_pdf
from siscontrol.general_utility import generar_pdf, admin_log_addition, admin_log_change, create_code_activation

from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import *

from datetime import *
from datetime import timedelta

class Lista_Categoria(ListView):
	model = Categoria
	template_name = 'categoria/lista_categoria.html'
	context_object_name = 'categorias'

class Crear_Categoria(CreateView):
	template_name = 'categoria/crear_categoria.html'
	form_class = CategoriaForm
	success_url = reverse_lazy('lista_categoria')

	@method_decorator(permission_required('articulo.add_categoria', reverse_lazy('lista_categoria')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Categoria, self).dispatch(*args, **kwargs)

class Modificar_Categoria(UpdateView):
	model = Categoria
	template_name = 'categoria/modificar_categoria.html'
	form_class = CategoriaForm
	success_url = reverse_lazy('lista_categoria')

	@method_decorator(permission_required('articulo.change_categoria', reverse_lazy('lista_categoria')))
	def dispatch(self, *args, **kwargs):
		return super(Modificar_Categoria, self).dispatch(*args, **kwargs)

class Eliminar_Categoria(DeleteView):
	model =  Categoria
	template_name =  'categoria/eliminar_categoria.html'
	success_url = reverse_lazy('lista_categoria')

	@method_decorator(permission_required('articulo.delete_categoria', reverse_lazy('lista_categoria')))
	def dispatch(self, *args, **kwargs):
		return super(Eliminar_Categoria, self).dispatch(*args, **kwargs)

def Crear_Categoria_PDF(request):
	categoria = Categoria.objects.all()
	html = render_to_string('categoria/pdf_categoria.html', {'categoria':categoria})
	return generar_pdf(html)


def Detalle_Categoria(request, categoria_id):
	categoria = get_object_or_404(Categoria, pk = categoria_id)
	articulos = Articulo.objects.filter(categoria = categoria)
	return render(request, 'categoria/lista_detalle.html', {
		'categoria':categoria,
		'articulos':articulos,
		})
#---------------------------------------------------------------------------
class Lista_Almacen(ListView):
	model =  Almacen
	template_name = 'almacen/lista_almacen.html'
	context_object_name = 'almacenes'

class Crear_Almacen(CreateView):
	template_name = 'almacen/crear_almacen.html'
	form_class = AlmacenForm
	success_url = reverse_lazy('lista_almacen')

	@method_decorator(permission_required('articulo.add_almacen', reverse_lazy('lista_almacen')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Almacen, self).dispatch(*args, **kwargs)

def new_almacen(request):
	if request.method == 'POST':
		form = AlmacenForm(request.POST)
		if form.is_valid():
			almacen = form.save()
			code = create_code_activation()
			code = '%s'%(code)
			almacen.cod_alm = code
			almacen.save()
			return HttpResponseRedirect('/almacen/')
	else:
		form = AlmacenForm()
	return render(request, 'almacen/crear_almacen.html', {
		'form':form,
		})

class Modificar_Almacen(UpdateView):
	model = Almacen
	template_name = 'almacen/modificar_almacen.html'
	form_class = AlmacenForm
	success_url = reverse_lazy('lista_almacen')

	@method_decorator(permission_required('articulo.change_almacen', reverse_lazy('lista_almacen')))
	def dispatch(self, *args, **kwargs):
		return super(Modificar_Almacen, self).dispatch(*args, **kwargs)

class Eliminar_Almacen(DeleteView):
	model = Almacen
	template_name = 'almacen/eliminar_almacen.html'
	success_url = reverse_lazy('lista_almacen')

	@method_decorator(permission_required('articulo.delete_almacen', reverse_lazy('lista_almacen')))
	def dispatch(self, *args, **kwargs):
		return super(Eliminar_Almacen, self).dispatch(*args, **kwargs)
#---------------------------------------------------------------------------
class Lista_Medida(ListView):
	model = Tipo_Medida
	template_name = 'medida/lista_medida.html'
	context_object_name = 'medidas'

class Crear_Medida(CreateView):
	template_name = 'medida/crear_medida.html'
	form_class = MedidaForm
	success_url = reverse_lazy('lista_medida')

	@method_decorator(permission_required('articulo.add_tipo_medida', reverse_lazy('lista_medida')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Medida, self).dispatch(*args, **kwargs)

class Modificar_Medida(UpdateView):
	model = Tipo_Medida
	template_name = 'medida/modificar_medida.html'
	form_class = MedidaForm
	success_url = reverse_lazy('lista_medida')

	@method_decorator(permission_required('articulo.change_tipo_medida', reverse_lazy('lista_medida')))
	def dispatch(self, *args, **kwargs):
		return super(Modificar_Medida, self).dispatch(*args, **kwargs)

class Eliminar_Medida(DeleteView):
	model = Tipo_Medida
	template_name = 'medida/eliminar_medida.html'
	success_url = reverse_lazy('lista_medida')

	@method_decorator(permission_required('articulo.delete_tipo_medida', reverse_lazy('lista_medida')))
	def dispatch(self, *args, **kwargs):
		return super(Eliminar_Medida, self).dispatch(*args, **kwargs)
#---------------------------------------------------------------------------
class Lista_Articulo(ListView):
	model = Articulo
	template_name = 'articulo/lista_articulo.html'
	context_object_name = 'articulos'

class Crear_Articulo(CreateView):
	template_name = 'articulo/crear_articulo.html'
	form_class = ArticuloForm
	success_url = reverse_lazy('lista_articulo')

	@method_decorator(permission_required('articulo.add_articulo', reverse_lazy('lista_articulo')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Articulo, self).dispatch(*args, **kwargs)

@login_required(login_url = '/')
def new_articulo(request):
	if request.method == 'POST':
		form = ArticuloForm(request.POST)
		if form.is_valid():
			articulo = form.save()
			code = create_code_activation()
			code = '%s'%(code)
			articulo.cod_art = code
			articulo.save()
			return HttpResponseRedirect('/material/')
	else:
		form = ArticuloForm()
	return render(request, 'articulo/crear_articulo.html', {
		'form':form,
		})


class Modificar_Articulo(UpdateView):
	model = Articulo
	template_name = 'articulo/modificar_articulo.html'
	form_class = ArticuloForm
	success_url = reverse_lazy('lista_articulo')

	@method_decorator(permission_required('articulo.change_articulo', reverse_lazy('lista_articulo')))
	def dispatch(self, *args, **kwargs):
		return super(Modificar_Articulo, self).dispatch(*args, **kwargs)

class Eliminar_Articulo(DeleteView):
	model = Articulo
	template_name = 'articulo/eliminar_articulo.html'
	success_url = reverse_lazy('lista_articulo')

	@method_decorator(permission_required('articulo.delete_articulo', reverse_lazy('lista_articulo')))
	def dispatch(self, *args, **kwargs):
		return super(Eliminar_Articulo, self).dispatch(*args, **kwargs)

class Detalle_Articulo(DetailView):
	model = Articulo
	template_name = 'articulo/detalle_articulo.html'

	@method_decorator(permission_required('articulo.ver_detalle_articulo', reverse_lazy('lista_articulo')))
	def dispatch(self, *args, **kwargs):
		return super(Detalle_Articulo, self).dispatch(*args, **kwargs)
#---------------------------------------------------------------------------
class Lista_Ingreso(ListView):
	model = Ingreso
	template_name = 'ingreso/lista_ingreso.html'
	context_object_name = 'ingresos'

class Detalle_Ingreso(DetailView):
	model = Ingreso
	template_name = 'ingreso/detalle_ingreso.html'

	@method_decorator(permission_required('articulo.ver_detalle_ingreso', reverse_lazy('lista_ingreso')))
	def dispatch(self, *args, **kwargs):
		return super(Detalle_Ingreso, self).dispatch(*args, **kwargs)

#@permission_required('articulo.add_articulo', login_url='/inicio/')
@login_required(login_url = '/')
def Crear_Ingreso(request, id_art):
	art = get_object_or_404(Articulo, id = id_art)
	if request.method == 'GET':
		form = IngresoForm(instance = art )
	else:
		form = IngresoForm(request.POST)
		if form.is_valid():
			cantidad = int(request.POST['cantidad'])
			precio_u = float(request.POST['precio_u'])
			precio_total = float(cantidad * precio_u)
			art.stock_actual = art.stock_actual + cantidad
			art.save()
			ingreso = form.save(commit=False)
			ingreso.articulo = art
			ingreso.precio_t = precio_total
			ingreso.salida = 0
			ingreso.saldo = cantidad
			ingreso.save()
			admin_log_change(request, request.user, 'Ingreso registrado')
			return HttpResponseRedirect('/material/')
	ctx = {'form':form,'art':art}
	return render(request, 'ingreso/crear_ingreso.html', ctx)

	@method_decorator(permission_required('articulo.add_ingreso', reverse_lazy('lista_ingreso')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Ingreso, self).dispatch(*args, **kwargs)

def Crear_PDF_Ingreso(request, id_ing):
    ing = get_object_or_404(Ingreso, pk = id_ing)
    html = render_to_string('ingreso/kardex_ingreso.html', {'ing': ing})
    return generar_pdf(html)
#-------------------------------pdf total ingreso--------------------------------------------
def write_pdf(template_src, context_dict):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-16")), result)
	if not pdf.err:
		return http.HttpResponse(result.getvalue(), content_type='application/pdf')
	return http.HttpResponse('Ocurrio un error al generar el reporte %s' % cgi.escape(html))

def Crear_Reporte_Ingresos(request):
	hora = datetime.today()

	if request.method == "POST":
		formbusqueda = RangoForm(request.POST)
		if formbusqueda.is_valid():
			fecha_in = formbusqueda.cleaned_data['fecha_i']
			fecha_fi = formbusqueda.cleaned_data['fecha_f']
			rango = Ingreso.objects.filter(fecha_i__gte=(fecha_in), fecha_i__lte=(fecha_fi)).order_by('fecha_i')

			total_i = 0
			for exp in rango:
				total_i = ((exp.precio_t) + (total_i))

			return write_pdf ('ingreso/reporte_lista_ingresos.html',{'rango' : rango, 'total_i':total_i, 'hora':hora})
		else:
			error = "Hay un error en las fechas proporcionadas"
			return render(request, 'reportes/reporte_ingresos.html', {'error': error})
	return render(request, 'reportes/reporte_ingresos.html', {'rangoform': RangoForm()})

#----------------------------------pdf total salidas-----------------------------------------
@login_required(login_url = '/')
def Crear_Reporte_Salidas(request):
	hora = datetime.today()

	if request.method == "POST":
		formbusqe = RangoForm(request.POST)
		if formbusqe.is_valid():
			fecha_ini = formbusqe.cleaned_data['fecha_i']
			fecha_fin = formbusqe.cleaned_data['fecha_f']
			rango_f = Salida.objects.filter(fecha_s__gte=(fecha_ini), fecha_s__lte=(fecha_fin)).order_by('fecha_s')

			total_s = 0
			for sl in rango_f:
				total_s = ((sl.precio) + (total_s))


			return write_pdf('salida/reporte_lista_salida.html', {'rango_f':rango_f,  'total_s':total_s, 'hora':hora})
		else:
			error = "Hay un error en las fechas proporcionadas"
			return render(request, 'reportes/reportes_salida.html', {'error':error})
	return render(request, 'reportes/reportes_salida.html', {'rangoform':RangoForm()})


#---------------------------------------------------------------------------

class Lista_Salida(ListView):
	model =  Salida
	template_name =  'salida/lista_salida.html'
	context_object_name = 'salidas'

class Detalle_Salida(DetailView):
	model = Salida
	template_name = 'salida/detalle_salida.html'

	#@method_decorator(permission_required('salida.ver_detalle_salida', reverse_lazy('lista_salida')))
	def dispatch(self, *args, **kwargs):
		return super(Detalle_Salida, self).dispatch(*args, **kwargs)

@login_required(login_url = '/')
def Crear_Salida(request, id_articulo):
	articulo = get_object_or_404(Articulo, pk = id_articulo)
	if request.method == 'POST':
		form = SalidaForm(request.POST)
		if form.is_valid():
			entradas = Ingreso.objects.filter(saldo__gt=0, articulo=articulo)
			cantidad = int(request.POST['cantidad'])
			stock =  articulo.stock_actual
			if cantidad <= stock:
				articulo.stock_actual = articulo.stock_actual - cantidad
				articulo.save()
				salida = form.save(commit=False)
				costo = 0.0
				for e in entradas:
					if cantidad > 0:
						#print cantidad
						if e.saldo >= cantidad:
							e.saldo = e.saldo - cantidad
							e.salida = cantidad + e.salida
							e.save()
							costo = costo + (cantidad * e.precio_u)
							cantidad = cantidad - e.saldo
						else:
							cantidad = cantidad - e.saldo
							e.salida = e.saldo + e.salida
							costo = costo + (e.saldo * e.precio_u)
							e.saldo = 0
							e.save()
				salida.precio = costo
				salida.articulo = articulo
				salida.save()
			else:
				return HttpResponseRedirect('/error/stock/')
			return HttpResponseRedirect('/salida/')
	else:
		form = SalidaForm()
	ctx = {'form':form, 'sal':articulo}
	return render(request, 'salida/crear_salida.html', ctx)

	@method_decorator(permission_required('articulo.add_salida', reverse_lazy('lista_salida')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Salida, self).dispatch(*args, **kwargs)

def write_PDF(html):
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type = 'application/pdf')
	else:
		return HttpResponse("Error al generar el pdf: %s" % cgi.escape(html))

def Crear_PDF_Salida(request, id_sal):
	sal = get_object_or_404(Salida, id = id_sal)
	html = render_to_string('salida/kardex_salida.html', {'sal':sal},)
	return write_PDF(html)

class Error_Stock(TemplateView):
	template_name = 'salida/error_stock.html'
#---------------------------------------------------------------------------
@login_required(login_url = '/')
def kardex_movimientos(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk = articulo_id)
    entradas = Ingreso.objects.all().first()
    fecha_ini = entradas.fecha_i
    fechas = []
    fecha = fecha_ini
    flag = True
    while flag:
        ingresos = Ingreso.objects.filter(fecha_i__day=fecha.day, fecha_i__month=fecha.month, fecha_i__year=fecha.year, articulo=articulo)
        #print fecha
        for i in ingresos:
            #print i.fecha_i
            #print i.id
            fechas += [
                {'fecha':fecha, 'concepto':'ingreso', 'id':i.id}
            ]
        salidas = Salida.objects.filter(fecha_s__day=fecha.day, fecha_s__month=fecha.month, fecha_s__year=fecha.year, articulo=articulo)
        for s in salidas:
            fechas += [
                {'fecha': fecha, 'concepto': 'salida', 'id':s.id}
            ]
        fecha += timedelta(days=1)

        if fecha.strftime('%Y-%m-%d') > datetime.now().strftime('%Y-%m-%d'):
            flag = False
    return render(request, 'articulo/kardex_mov.html', {
        'articulo':articulo,
        'fechas':fechas,
    })

@login_required(login_url = '/')
def Crear_PDF_Movimiento(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk = articulo_id)
    entradas = Ingreso.objects.all().first()
    fecha_ini = entradas.fecha_i
    fechas = []
    fecha = fecha_ini
    flag = True
    while flag:
        ingresos = Ingreso.objects.filter(fecha_i__day=fecha.day, fecha_i__month=fecha.month, fecha_i__year=fecha.year, articulo=articulo)
        #print fecha
        for i in ingresos:
            #print i.fecha_i
            #print i.id
            fechas += [
                {'fecha':fecha, 'concepto':'ingreso', 'id':i.id}
            ]
        salidas = Salida.objects.filter(fecha_s__day=fecha.day, fecha_s__month=fecha.month, fecha_s__year=fecha.year, articulo=articulo)
        for s in salidas:
            fechas += [
                {'fecha': fecha, 'concepto': 'salida', 'id':s.id}
            ]
        fecha += timedelta(days=1)

        if fecha.strftime('%Y-%m-%d') > datetime.now().strftime('%Y-%m-%d'):
            flag = False
    html = render_to_string('reportes/kardex_mov_pdf.html', {
        'articulo':articulo,
        'fechas':fechas,
    })
    return generar_pdf(html)
    generar_pdf(html)
