from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from aplication.core.models import Cargo
from aplication.core.forms.cargo import CargoForm

class CargoListView(LoginRequiredMixin, ListView):
    template_name = "core/cargo/list.html"
    model = Cargo
    context_object_name = "cargos"
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        return self.model.objects.filter(nombre__icontains=query).order_by("nombre")

class CargoCreateView(LoginRequiredMixin, CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = "core/cargo/form.html"
    success_url = reverse_lazy("core:cargo_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Cargo '{self.object.nombre}' creado con éxito.")
        return response

class CargoUpdateView(LoginRequiredMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = "core/cargo/form.html"
    success_url = reverse_lazy("core:cargo_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Cargo '{self.object.nombre}' actualizado con éxito.")
        return response

class CargoDeleteView(LoginRequiredMixin, DeleteView):
    model = Cargo
    success_url = reverse_lazy("core:cargo_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f"Cargo '{self.object.nombre}' eliminado con éxito.")
        return super().delete(request, *args, **kwargs)

class CargoDetailView(LoginRequiredMixin, DetailView):
    model = Cargo

    def get(self, request, *args, **kwargs):
        cargo = self.get_object()
        data = {
            "id": cargo.id,
            "nombre": cargo.nombre,
            "descripcion": cargo.descripcion,
            "activo": "Sí" if cargo.activo else "No",
        }
        return JsonResponse(data)
