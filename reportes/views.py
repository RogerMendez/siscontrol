# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template.loader import render_to_string

from siscontrol.general_utility import generar_pdf

from articulo.models import Articulo, Ingreso, Salida

from reportes.forms import FechasSearchForm
from django.contrib.auth.decorators import login_required

from datetime import date
import datetime

@login_required(login_url = '/')
def report_ingreso(request):
    articulos = Articulo.objects.all()
    return render(request, 'report/art_ingresos.html', {
        'articulos':articulos,
    })

@login_required(login_url = '/')
def detalle_ingreso(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk = articulo_id)
    ingresos = Ingreso.objects.filter(articulo=articulo)
    return render(request, 'report/detail_ingreso.html', {
        'articulo':articulo,
        'ingresos':ingresos,
    })

@login_required(login_url = '/')
def pdf_detalle_ingreso(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    ingresos = Ingreso.objects.filter(articulo=articulo)
    html = render_to_string('report/pdf_detalle_ingreso.html', {
        'articulo': articulo,
        'ingresos': ingresos,
    })
    return generar_pdf(html)

@login_required(login_url = '/')
def detalle_ingreso_fechas(request, articulo_id):
    fecha_ini = datetime.datetime.now()
    fecha_fin = datetime.datetime.now()
    articulo = get_object_or_404(Articulo, pk = articulo_id)
    form = FechasSearchForm(request.GET or None)
    if form.is_valid():
        fecha_ini = form.cleaned_data['fecha_ini']
        fecha_fin = form.cleaned_data['fecha_fin']
    ingresos = Ingreso.objects.filter(
        articulo=articulo,
        fecha_i__year__gte=fecha_ini.year, fecha_i__month__gte=fecha_ini.month, fecha_i__day__gte=fecha_ini.day,
        fecha_i__year__lte=fecha_fin.year, fecha_i__month__lte=fecha_fin.month, fecha_i__day__lte=fecha_fin.day
    )
    return render(request, 'report/detail_ingreso_fechas.html', {
        'articulo':articulo,
        'ingresos':ingresos,
        'form':form,
        'fecha_ini':fecha_ini,
        'fecha_fin':fecha_fin,
    })

@login_required(login_url = '/')
def pdf_detalle_ingreso_fechas(request, articulo_id, year, month, day, year1, month1, day1):
    articulo = get_object_or_404(Articulo, pk = articulo_id)
    fecha_ini = date(int(year), int(month), int(day))
    fecha_fin = date(int(year1), int(month1), int(day1))
    ingresos = Ingreso.objects.filter(
        articulo=articulo,
        fecha_i__year__gte=fecha_ini.year, fecha_i__month__gte=fecha_ini.month, fecha_i__day__gte=fecha_ini.day,
        fecha_i__year__lte=fecha_fin.year, fecha_i__month__lte=fecha_fin.month, fecha_i__day__lte=fecha_fin.day
    )
    html = render_to_string('report/pdf_detalle_ingreso_fechas.html', {
        'articulo':articulo,
        'ingresos':ingresos,
        'fecha_ini':fecha_ini,
        'fecha_fin':fecha_fin,
    })
    return generar_pdf(html)

@login_required(login_url = '/')
def report_salida(request):
    articulos = Articulo.objects.all()
    return render(request, 'report/art_salida.html', {
        'articulos':articulos,
    })

@login_required(login_url = '/')
def detalle_salidas(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk = articulo_id)
    salidas = Salida.objects.filter(articulo=articulo)
    return render(request, 'report/detail_salida.html', {
        'articulo':articulo,
        'salidas':salidas,
    })

@login_required(login_url = '/')
def pdf_detalle_salida(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    salidas = Salida.objects.filter(articulo=articulo)
    html = render_to_string('report/pdf_detalle_salida.html', {
        'articulo': articulo,
        'salidas': salidas,
    })
    return generar_pdf(html)

@login_required(login_url = '/')
def detalle_salida_fechas(request, articulo_id):
    fecha_ini = datetime.datetime.now()
    fecha_fin = datetime.datetime.now()
    articulo = get_object_or_404(Articulo, pk = articulo_id)
    form = FechasSearchForm(request.GET or None)
    if form.is_valid():
        fecha_ini = form.cleaned_data['fecha_ini']
        fecha_fin = form.cleaned_data['fecha_fin']
    salidas = Salida.objects.filter(
        articulo=articulo,
        fecha_s__year__gte=fecha_ini.year, fecha_s__month__gte=fecha_ini.month, fecha_s__day__gte=fecha_ini.day,
        fecha_s__year__lte=fecha_fin.year, fecha_s__month__lte=fecha_fin.month, fecha_s__day__lte=fecha_fin.day
    )
    return render(request, 'report/detail_salida_fechas.html', {
        'articulo':articulo,
        'salidas':salidas,
        'form':form,
        'fecha_ini':fecha_ini,
        'fecha_fin':fecha_fin,
    })

@login_required(login_url = '/')
def pdf_detalle_salida_fechas(request, articulo_id, year, month, day, year1, month1, day1):
    articulo = get_object_or_404(Articulo, pk = articulo_id)
    fecha_ini = date(int(year), int(month), int(day))
    fecha_fin = date(int(year1), int(month1), int(day1))
    salidas = Salida.objects.filter(
        articulo=articulo,
        fecha_s__year__gte=fecha_ini.year, fecha_s__month__gte=fecha_ini.month, fecha_s__day__gte=fecha_ini.day,
        fecha_s__year__lte=fecha_fin.year, fecha_s__month__lte=fecha_fin.month, fecha_s__day__lte=fecha_fin.day
    )
    html = render_to_string('report/pdf_detalle_salidas_fechas.html', {
        'articulo':articulo,
        'salidas':salidas,
        'fecha_ini':fecha_ini,
        'fecha_fin':fecha_fin,
    })
    return generar_pdf(html)