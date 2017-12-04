from django import forms
from .models import *
#from django.core.exceptions import ValidationError

import datetime

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ['cod_cat', 'descripcion']
		widgets = {'cod_cat' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),
					'descripcion' : forms.TextInput(attrs={'class':'form-control',}),}

	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if Categoria.objects.filter(descripcion = descripcion):
			raise forms.ValidationError( 'Nombre de cuenta contable ya registrado.')
		return descripcion

class AlmacenForm(forms.ModelForm):
	class Meta:
		model = Almacen
		fields = ['descripcion']
		widgets = {'descripcion' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),}

	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if Almacen.objects.filter(descripcion = descripcion):
			raise forms.ValidationError( 'Nombre de ubicacion ya registrado.')
		return descripcion


class MedidaForm(forms.ModelForm):
	class Meta:
		model = Tipo_Medida
		fields = ['descripcion']
		widgets = {'descripcion' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),}

	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if Tipo_Medida.objects.filter(descripcion = descripcion):
			raise forms.ValidationError( 'Nombre de unidad_medida ya registrado.')
		return descripcion

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Articulo
		exclude = ['stock_actual']
		fields = ['descripcion', 'marca', 'modelo', 'proveedor', 'categoria', 'almacen', 'medida']
		widgets = {'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
				   'marca': forms.TextInput(attrs={'class': 'form-control'}),
				   'modelo': forms.TextInput(attrs={'class': 'form-control'}),
				   'proveedor': forms.Select(attrs={'class': 'form-control'}),
				   'categoria': forms.Select(attrs={'class': 'form-control'}),
				   'almacen': forms.Select(attrs={'class': 'form-control'}),
				   'medida': forms.Select(attrs={'class': 'form-control'}),
				   }

class IngresoForm(forms.ModelForm):
	class Meta:
		model = Ingreso
		exclude = ['articulo', 'precio_t', 'total_i']
		fields = ['empleado', 'cantidad', 'precio_u', 'observacion', 'factura',]
		widgets = {
				'empleado': forms.Select(attrs={'class': 'form-control'}),
				'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
				'precio_u': forms.TextInput(attrs={'class': 'form-control'}),
				'observacion': forms.TextInput(attrs={'class': 'form-control'}),
				'factura': forms.TextInput(attrs={'class': 'form-control'}),}

class SalidaForm(forms.ModelForm):
	class Meta:
		model = Salida
		exclude = ['ingreso', 'total_s']
		fields = ['empleado', 'cantidad', 'observacion']
		widgets = {
					'empleado': forms.Select(attrs={'class': 'form-control'}),
				'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
				'observacion': forms.TextInput(attrs={'class': 'form-control'}),}

class RangoForm (forms.Form):
	fecha_i = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_i', 'data-date-format':'dd/mm/yyyy', 'placeholder':'dd/mm/yyyy'}))
	fecha_f = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_f', 'data-date-format':'dd/mm/yyyy', 'placeholder':'dd/mm/yyyy'}))

	def clean_fecha_i(self):
		today = datetime.datetime.now()
		data = self.cleaned_data['fecha_i']
		if data.strftime('%d-%m-%Y') > today.strftime('%d-%m-%Y'):
			raise forms.ValidationError('No puede selecionar una fecha mayor a la  actual')
		return data

	def clean_fecha_f(self):
		today = datetime.datetime.now ()
		data = self.cleaned_data['fecha_f']
		if data.strftime('%d-%m-%Y') > today.strftime('%d-%m-%Y'):
			raise forms.ValidationError('No puede selecionar una fecha mayor a la  actual')
		return data
