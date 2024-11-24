from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.contrib import messages
from aplication.core.models import TipoMedicamento
from aplication.core.forms.tipo_medicamento import TipoMedicamentoForm
from doctor.utils import save_audit

class TipoMedicamentoListView(ListView):
    model = TipoMedicamento
    template_name = "core/tipo_medicamento/list.html"
    context_object_name = "tipos"
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return TipoMedicamento.objects.filter(nombre__icontains=query)
        return TipoMedicamento.objects.all()


class TipoMedicamentoCreateView(SuccessMessageMixin, CreateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = "core/tipo_medicamento/form.html"
    success_url = reverse_lazy("core:tipo_medicamento_list")
    success_message = "Tipo de Medicamento creado exitosamente."

    def form_valid(self, form):
        # Guardar el formulario y registrar la auditoría
        response = super().form_valid(form)
        save_audit(self.request, self.object, "A")  # "A" para Adición
        return response


class TipoMedicamentoUpdateView(SuccessMessageMixin, UpdateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = "core/tipo_medicamento/form.html"
    success_url = reverse_lazy("core:tipo_medicamento_list")
    success_message = "Tipo de Medicamento actualizado exitosamente."


class TipoMedicamentoDeleteView(DeleteView):
    model = TipoMedicamento
    template_name = "includes/confirm_delete_modal.html"
    success_url = reverse_lazy("core:tipo_medicamento_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Tipo de Medicamento eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)


class TipoMedicamentoDetailView(DetailView):
    model = TipoMedicamento

    def get(self, request, *args, **kwargs):
        tipo = self.get_object()
        data = {
            "id": tipo.id,
            "nombre": tipo.nombre,
            "descripcion": tipo.descripcion,
            "activo": tipo.activo,
        }
        return JsonResponse(data)
