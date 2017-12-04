from django.views.generic import UpdateView, CreateView, ListView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .models import Proveedor
from .forms import ProveedorForm


class Lista_Proveedor(ListView):
	model = Proveedor
	template_name = 'proveedor/proveedores.html'
	context_object_name = 'proveedores'

class Crear_Proveedor(CreateView):
	template_name = 'proveedor/crear_proveedor.html'
	form_class = ProveedorForm
	success_url = reverse_lazy('proveedores:lista_proveedor')

	@method_decorator(permission_required('proveedor.add_proveedor', reverse_lazy('proveedores:lista_proveedor')))
	def dispatch(self, *args, **kwargs):
		return super(Crear_Proveedor, self).dispatch(*args, **kwargs)

class Modificar_Proveedor(UpdateView):
	model =  Proveedor
	template_name = 'proveedor/modificar_proveedor.html'
	form_class = ProveedorForm
	success_url = reverse_lazy('proveedores:lista_proveedor')

	@method_decorator(permission_required('proveedor.change_proveedor', reverse_lazy('proveedores:lista_proveedor')))
	def dispatch(self, *args, **kwargs):
		return super(Modificar_Proveedor, self).dispatch(*args, **kwargs)

class Detalle_Proveedor(DetailView):
	model = Proveedor
	template_name = 'proveedor/detalle_proveedor.html'

	@method_decorator(permission_required('proveedor.ver_detalle_proveedor', reverse_lazy('proveedores:lista_proveedor')))
	def dispatch(self, *args, **kwargs):
		return super(Detalle_Proveedor, self).dispatch(*args, **kwargs)

class Eliminar_Proveedor(DeleteView):
	model = Proveedor
	template_name = 'proveedor/eliminar_proveedor.html'
	success_url = reverse_lazy('proveedores:lista_proveedor')

	@method_decorator(permission_required('proveedor.delete_proveedor', reverse_lazy('proveedores:lista_proveedor')))
	def dispatch(self, *args, **kwargs):
		return super(Eliminar_Proveedor, self).dispatch(*args, **kwargs)