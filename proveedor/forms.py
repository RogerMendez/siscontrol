from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = ['ci', 'nombre', 'apellidos', 'genero', 'razon_social', 'direccion', 'telefono', 'correo']
		widgets = {'ci' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),
		'nombre' : forms.TextInput(attrs={'class':'form-control'}),
		'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
		'genero' : forms.Select(attrs={'class':'form-control'}),
		'razon_social' : forms.TextInput(attrs={'class':'form-control'}),
		'direccion' : forms.TextInput(attrs={'class':'form-control'}),
		'telefono' : forms.TextInput(attrs={'class':'form-control'}),
		'correo' : forms.TextInput(attrs={'class':'form-control'}),}
