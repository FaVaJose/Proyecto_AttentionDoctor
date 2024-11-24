from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.contrib import messages
from aplication.core.models import Empleado
from aplication.core.forms.empleado import EmpleadoForm

class EmpleadoListView(ListView):
    model = Empleado
    template_name = "core/empleado/list.html"
    context_object_name = "empleados"
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Empleado.objects.filter(
                nombres__icontains=query
            ) | Empleado.objects.filter(apellidos__icontains=query)
        return Empleado.objects.all()


class EmpleadoCreateView(SuccessMessageMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "core/empleado/form.html"
    success_url = reverse_lazy("core:empleado_list")
    success_message = "Empleado creado exitosamente."


class EmpleadoUpdateView(SuccessMessageMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "core/empleado/form.html"
    success_url = reverse_lazy("core:empleado_list")
    success_message = "Empleado actualizado exitosamente."


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "includes/confirm_delete_modal.html"
    success_url = reverse_lazy("core:empleado_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Empleado eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)


class EmpleadoDetailView(DetailView):
    model = Empleado

    def get(self, request, *args, **kwargs):
        empleado = self.get_object()
        data = {
            'id': empleado.id,
            'nombre_completo': empleado.nombre_completo,
            'cargo': str(empleado.cargo),
            'sueldo': f"{empleado.sueldo:.2f}",
            'direccion': empleado.direccion,
            'activo': empleado.activo,
            'foto': empleado.foto.url if empleado.foto else '/static/img/empleado_default.jpg',
        }
        return JsonResponse(data)
