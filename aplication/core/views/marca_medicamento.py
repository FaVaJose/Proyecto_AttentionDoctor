from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib import messages
from aplication.core.models import MarcaMedicamento
from aplication.core.forms.marca_medicamento import MarcaMedicamentoForm
from doctor.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class MarcaMedicamentoListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "core/marca_medicamento/list.html"
    model = MarcaMedicamento
    context_object_name = "marcas"

class MarcaMedicamentoCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = "core/marca_medicamento/form.html"
    success_url = reverse_lazy("core:marca_medicamento_list")

    def form_valid(self, form):
        messages.success(self.request, f"Marca '{form.instance.nombre}' creada con éxito.")
        return super().form_valid(form)

class MarcaMedicamentoUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = "core/marca_medicamento/form.html"
    success_url = reverse_lazy("core:marca_medicamento_list")

    def form_valid(self, form):
        messages.success(self.request, f"Marca '{form.instance.nombre}' actualizada con éxito.")
        return super().form_valid(form)

class MarcaMedicamentoDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = MarcaMedicamento
    success_url = reverse_lazy("core:marca_medicamento_list")

    def delete(self, request, *args, **kwargs):
        marca = self.get_object()
        messages.success(self.request, f"Marca '{marca.nombre}' eliminada con éxito.")
        return super().delete(request, *args, **kwargs)

class MarcaMedicamentoDetailView(LoginRequiredMixin, DetailView):
    model = MarcaMedicamento

    def get(self, request, *args, **kwargs):
        marca = self.get_object()
        data = {
            "nombre": marca.nombre,
            "descripcion": marca.descripcion,
            "activo": "Sí" if marca.activo else "No",
        }
        return JsonResponse(data)
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib import messages
from aplication.core.models import MarcaMedicamento
from aplication.core.forms.marca_medicamento import MarcaMedicamentoForm
from doctor.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class MarcaMedicamentoListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "core/marca_medicamento/list.html"
    model = MarcaMedicamento
    context_object_name = "marcas"

class MarcaMedicamentoCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = "core/marca_medicamento/form.html"
    success_url = reverse_lazy("core:marca_medicamento_list")

    def form_valid(self, form):
        messages.success(self.request, f"Marca '{form.instance.nombre}' creada con éxito.")
        return super().form_valid(form)

class MarcaMedicamentoUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = "core/marca_medicamento/form.html"
    success_url = reverse_lazy("core:marca_medicamento_list")

    def form_valid(self, form):
        messages.success(self.request, f"Marca '{form.instance.nombre}' actualizada con éxito.")
        return super().form_valid(form)

class MarcaMedicamentoDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = MarcaMedicamento
    success_url = reverse_lazy("core:marca_medicamento_list")

    def delete(self, request, *args, **kwargs):
        marca = self.get_object()
        messages.success(self.request, f"Marca '{marca.nombre}' eliminada con éxito.")
        return super().delete(request, *args, **kwargs)

class MarcaMedicamentoDetailView(LoginRequiredMixin, DetailView):
    model = MarcaMedicamento

    def get(self, request, *args, **kwargs):
        marca = self.get_object()
        data = {
            "nombre": marca.nombre,
            "descripcion": marca.descripcion,
            "activo": "Sí" if marca.activo else "No",
        }
        return JsonResponse(data)
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib import messages
from aplication.core.models import MarcaMedicamento
from aplication.core.forms.marca_medicamento import MarcaMedicamentoForm
from doctor.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class MarcaMedicamentoListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "core/marca_medicamento/list.html"
    model = MarcaMedicamento
    context_object_name = "marcas"

class MarcaMedicamentoCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = "core/marca_medicamento/form.html"
    success_url = reverse_lazy("core:marca_medicamento_list")

    def form_valid(self, form):
        messages.success(self.request, f"Marca '{form.instance.nombre}' creada con éxito.")
        return super().form_valid(form)

class MarcaMedicamentoUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = "core/marca_medicamento/form.html"
    success_url = reverse_lazy("core:marca_medicamento_list")

    def form_valid(self, form):
        messages.success(self.request, f"Marca '{form.instance.nombre}' actualizada con éxito.")
        return super().form_valid(form)

class MarcaMedicamentoDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = MarcaMedicamento
    success_url = reverse_lazy("core:marca_medicamento_list")

    def delete(self, request, *args, **kwargs):
        marca = self.get_object()
        messages.success(self.request, f"Marca '{marca.nombre}' eliminada con éxito.")
        return super().delete(request, *args, **kwargs)

class MarcaMedicamentoDetailView(LoginRequiredMixin, DetailView):
    model = MarcaMedicamento

    def get(self, request, *args, **kwargs):
        marca = self.get_object()
        data = {
            "id": marca.id,
            "nombre": marca.nombre,
            "descripcion": marca.descripcion,
            "activo": marca.activo,
        }
        return JsonResponse(data)