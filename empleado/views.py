#from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import *

class Lista_Departamento(ListView):
	model =  Departamento
	template_name = 'departamento/lista_departamento.html'
	context_object_name = 'departamentos'

class Crear_Departamento(CreateView):
	template_name =  'departamento/crear_departamento.html'
	form_class = DepartamentoForm
	success_url = reverse_lazy('lista_departamento')

	@method_decorator(permission_required('empleado.add_departamento', reverse_lazy('lista_departamento')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Departamento, self).dispatch(*args, **kwargs)

class Modificar_Departamento(UpdateView):
	model = Departamento
	template_name = 'departamento/modificar_departamento.html'
	form_class = DepartamentoForm
	success_url =  reverse_lazy('lista_departamento')

	@method_decorator(permission_required('empleado.change_departamento', reverse_lazy('lista_departamento')))
	def dispatch(self, *args, **kwargs):
		return super(Modificar_Departamento, self).dispatch(*args, **kwargs)

class Eliminar_Departamento(DeleteView):
	model = Departamento
	template_name = 'departamento/eliminar_departamento.html'
	success_url = reverse_lazy('lista_departamento')

	@method_decorator(permission_required('empleado.delete_departamento', reverse_lazy('lista_departamento')))
	def dispatch(self, *args, **kwargs):
		return super(Eliminar_Departamento, self).dispatch(*args, **kwargs)
#---------------------------------------------------------------------------

class Lista_Empleado(ListView):
	model = Empleado
	template_name = 'empleado/lista_empleado.html'
	context_object_name = 'empleados'

class Crear_Empleado(CreateView):
	template_name = 'empleado/crear_empleado.html'
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleado')

	@method_decorator(permission_required('empleado.add_empleado', reverse_lazy('lista_empleado')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Empleado, self).dispatch(*args, **kwargs)


class Modificar_Empleado(UpdateView):
	model = Empleado
	template_name = 'empleado/modificar_empleado.html'
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleado')

	@method_decorator(permission_required('empleado.change_empleado', reverse_lazy('lista_empleado')))
	def dispatch(self, *args, **kwargs):
		return super(Modificar_Empleado, self).dispatch(*args, **kwargs)

class Eliminar_Empleado(DeleteView):
	model = Empleado
	template_name = 'empleado/eliminar_empleado.html'
	success_url = reverse_lazy('lista_empleado')

	@method_decorator(permission_required('empleado.delete_empleado', reverse_lazy('lista_empleado')))
	def dispatch(self, *args, **kwargs):
		return super(Eliminar_Empleado, self).dispatch(*args, **kwargs)

class Detalle_Empleado(DetailView):
	model = Empleado
	template_name = 'empleado/detalle_empleado.html'

	@method_decorator(permission_required('empleado.ver_detalle_empleado', reverse_lazy('lista_empleado')))
	def dispatch(self, *args, **kwargs):
		return super(Detalle_Empleado, self).dispatch(*args, **kwargs)