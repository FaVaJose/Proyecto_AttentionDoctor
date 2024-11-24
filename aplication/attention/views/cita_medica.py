from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.attention.models import CitaMedica
from aplication.attention.forms.cita_medica import CitaMedicaForm
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit


class CitaMedicaListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "attention/cita_medica/list.html"
    model = CitaMedica
    context_object_name = 'citas'

    def get_queryset(self):
        query = Q()
        paciente = self.request.GET.get('paciente')
        estado = self.request.GET.get('estado')

        if paciente:
            query.add(Q(paciente__nombres__icontains=paciente) | Q(paciente__apellidos__icontains=paciente), Q.AND)
        if estado:
            query.add(Q(estado=estado), Q.AND)

        return self.model.objects.filter(query).order_by('fecha', 'hora_cita')


class CitaMedicaCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = CitaMedica
    template_name = 'attention/cita_medica/form.html'
    form_class = CitaMedicaForm
    success_url = reverse_lazy('attention:cita_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = 'Crear Cita Médica'
        context['grabar'] = 'Crear Cita'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        cita = self.object
        save_audit(self.request, cita, action='A')
        messages.success(self.request, f"Éxito al crear la cita para {cita.paciente} el {cita.fecha}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))


class CitaMedicaUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = CitaMedica
    template_name = 'attention/cita_medica/form.html'
    form_class = CitaMedicaForm
    success_url = reverse_lazy('attention:cita_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = 'Actualizar Cita Médica'
        context['grabar'] = 'Actualizar Cita'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        cita = self.object
        save_audit(self.request, cita, action='M')
        messages.success(self.request, f"Éxito al actualizar la cita para {cita.paciente} el {cita.fecha}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))


class CitaMedicaDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = CitaMedica
    template_name = 'attention/cita_medica/delete_confirm.html'
    success_url = reverse_lazy('attention:cita_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description'] = f"¿Desea eliminar la cita de {self.object.paciente} programada para {self.object.fecha} a las {self.object.hora_cita}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f"Éxito al eliminar la cita de {self.object.paciente} el {self.object.fecha}.")
        return super().delete(request, *args, **kwargs)


class CitaMedicaDetailView(LoginRequiredMixin, DetailView):
    model = CitaMedica

    def get(self, request, *args, **kwargs):
        cita = self.get_object()
        data = {
            'id': cita.id,
            'paciente': str(cita.paciente),
            'fecha': cita.fecha.strftime('%Y-%m-%d'),
            'hora_cita': cita.hora_cita.strftime('%H:%M:%S'),
            'estado': cita.get_estado_display(),
        }
        return JsonResponse(data)