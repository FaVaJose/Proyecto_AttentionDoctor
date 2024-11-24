from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from aplication.core.models import Especialidad
from aplication.core.forms.especialidad import EspecialidadForm

# Listar Especialidades
class EspecialidadListView(ListView):
    model = Especialidad
    template_name = "core/especialidad/list.html"
    context_object_name = "especialidades"
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return self.model.objects.filter(nombre__icontains=query).order_by("nombre")
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = "Consulta de Especialidades"
        return context


# Crear Especialidad
class EspecialidadCreateView(SuccessMessageMixin, CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = "core/especialidad/form.html"
    success_url = reverse_lazy("core:especialidad_list")
    success_message = "Especialidad creada con éxito."

# Editar Especialidad
class EspecialidadUpdateView(SuccessMessageMixin, UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = "core/especialidad/form.html"
    success_url = reverse_lazy("core:especialidad_list")
    success_message = "Especialidad actualizada con éxito."

# Eliminar Especialidad
class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = "core/especialidad/confirm_delete.html"
    success_url = reverse_lazy("core:especialidad_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Especialidad eliminada con éxito.")
        return super().delete(request, *args, **kwargs)

# Detalles de Especialidad
class EspecialidadDetailView(DetailView):
    model = Especialidad

    def get(self, request, *args, **kwargs):
        especialidad = self.get_object()
        data = {
            "id": especialidad.id,
            "nombre": especialidad.nombre,
            "descripcion": especialidad.descripcion,
            "activo": "Sí" if especialidad.activo else "No",
        }
        return JsonResponse(data)
