from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.forms.tipo_sangre import TipoSangreForm
from aplication.core.models import TipoSangre
from doctor.utils import save_audit

class TipoSangreListView(ListView):
    model = TipoSangre
    template_name = "core/tipo_sangre/list.html"
    context_object_name = "tipos_sangre"
    paginate_by = 4

    def get_queryset(self):
        # Filtrar solo por el campo 'tipo'
        query = self.request.GET.get("q")
        queryset = self.model.objects.all()
        if query:
            queryset = queryset.filter(Q(tipo__icontains=query))
        return queryset


class TipoSangreCreateView(CreateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = "core/tipo_sangre/form.html"
    success_url = reverse_lazy("core:tipo_sangre_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        save_audit(self.request,self.object, action = 'A')
        messages.success(self.request, f"Éxito al crear el tipo de sangre: {form.instance.tipo}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class TipoSangreUpdateView(UpdateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = "core/tipo_sangre/form.html"
    success_url = reverse_lazy("core:tipo_sangre_list")

    def form_valid(self, form):
        messages.success(self.request, f"Éxito al actualizar el tipo de sangre: {form.instance.tipo}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al actualizar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class TipoSangreDeleteView(DeleteView):
    model = TipoSangre
    success_url = reverse_lazy("core:tipo_sangre_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f"Éxito al eliminar el tipo de sangre: {self.object.tipo}.")
        return super().delete(request, *args, **kwargs)

class TipoSangreDetailView(DetailView):
    model = TipoSangre

    def get(self, request, *args, **kwargs):
        tipo_sangre = self.get_object()
        data = {
            "id": tipo_sangre.id,
            "tipo": tipo_sangre.tipo,
            "descripcion": tipo_sangre.descripcion,
        }
        return JsonResponse(data)
