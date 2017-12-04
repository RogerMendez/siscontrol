from django import forms
#from django.forms import ModelForm, TextInput
from .models import *

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		fields = ['descripcion']
		widgets = {'descripcion' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),}


	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if Departamento.objects.filter(descripcion = descripcion):
			raise forms.ValidationError( 'Nombre de unidad ya registrado.')
		return descripcion

	'''
	def clean_descri(self):
		descripcion = self.cleaned_data.get('descripcion', '')
		if len(descripcion) < 0:
			raise forms.ValidationError("Ingrese por lomenos 1 letra")
		return descripcion'''

class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ['ci', 'nombre', 'apellidos', 'cargo', 'direccion', 'telefono', 'departamento']
		widgets = {'ci' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),
		'nombre' : forms.TextInput(attrs={'class':'form-control'}),
		'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
		'cargo' : forms.Select(attrs={'class':'form-control'}),
		'direccion' : forms.TextInput(attrs={'class':'form-control'}),
		'telefono' : forms.TextInput(attrs={'class':'form-control'}),
		'departamento' : forms.Select(attrs={'class':'form-control'}),}