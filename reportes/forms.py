from django.forms import ModelForm, TextInput
from django import forms

import datetime

class FechasSearchForm(forms.Form):
    fecha_ini = forms.DateField(label='Fecha de Inicio', widget=forms.TextInput(attrs={'type': 'date', 'required': 'required', 'class':'form-control' }))
    fecha_fin = forms.DateField(label='Fecha de Finalizacion', widget=forms.TextInput(attrs={'type': 'date', 'required': 'required', 'class':'form-control'}))
    def clean_fecha_ini(self):
        today = datetime.datetime.now()
        data = self.cleaned_data['fecha_ini']
        if data.strftime('%Y-%m-%d') > today.strftime('%Y-%m-%d'):
            raise forms.ValidationError('No Puede Seleccionar Una Fecha Mayor a la Actual')
        return data
    def clean_fecha_fin(self):
        today = datetime.datetime.now()
        data = self.cleaned_data['fecha_fin']
        if data.strftime('%Y-%m-%d') > today.strftime('%Y-%m-%d'):
            raise forms.ValidationError('No Puede Seleccionar Una Fecha Mayor a la Actual')
        return data
    '''def clean(self):
        cleaned_data = super(FechasSearchForm, self).clean()
        inicio = cleaned_data.get("fecha_ini")
        fin = cleaned_data.get("fecha_fin")
        if inicio.strftime('%Y-%m-%d') > fin.strftime('%Y-%m-%d'):
            print 'ERROR'
            #raise forms.ValidationError("La fecha de INICIO no puede ser Mayor a la fecha FIN")
            self.add_error('fecha_ini', "La fecha de INICIO no puede ser Mayor a la fecha de FINALIZACION")
    '''