from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from aplication.core.models import Medicamento
from aplication.core.forms.medicamento import MedicamentoForm

class MedicamentoListView(LoginRequiredMixin, ListView):
    template_name = "core/medicamento/list.html"
    model = Medicamento
    context_object_name = "medicamentos"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = self.model.objects.all()
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset

class MedicamentoCreateView(LoginRequiredMixin, CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = "core/medicamento/form.html"
    success_url = reverse_lazy("core:medicamento_list")

    def form_valid(self, form):
        messages.success(self.request, "Medicamento creado con éxito.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al crear el medicamento.")
        return self.render_to_response(self.get_context_data(form=form))

class MedicamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = "core/medicamento/form.html"
    success_url = reverse_lazy("core:medicamento_list")

    def form_valid(self, form):
        messages.success(self.request, "Medicamento actualizado con éxito.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al actualizar el medicamento.")
        return self.render_to_response(self.get_context_data(form=form))

class MedicamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicamento
    success_url = reverse_lazy("core:medicamento_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Medicamento eliminado con éxito.")
        return super().delete(request, *args, **kwargs)

class MedicamentoDetailView(LoginRequiredMixin, DetailView):
    model = Medicamento

    def get(self, request, *args, **kwargs):
        medicamento = self.get_object()
        data = {
            "id": medicamento.id,
            "tipo": str(medicamento.tipo),
            "marca_medicamento": str(medicamento.marca_medicamento),
            "nombre": medicamento.nombre,
            "descripcion": medicamento.descripcion,
            "concentracion": medicamento.concentracion,
            "cantidad": medicamento.cantidad,
            "precio": str(medicamento.precio),
            "comercial": medicamento.comercial,
            "activo": medicamento.activo,
        }
        return JsonResponse(data)