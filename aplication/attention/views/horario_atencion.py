from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.attention.models import HorarioAtencion
from aplication.attention.forms.horario_atencion import HorarioAtencionForm
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit


class HorarioAtencionListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "attention/horario_atencion/list.html"
    model = HorarioAtencion
    context_object_name = 'horarios'
    
    def get_queryset(self):
        query = Q()
        dia_semana = self.request.GET.get('dia_semana')
        activo = self.request.GET.get('activo')

        if dia_semana:
            query.add(Q(dia_semana__icontains=dia_semana), Q.AND)
        if activo in ["True", "False"]:
            query.add(Q(activo=activo == "True"), Q.AND)

        return self.model.objects.filter(query).order_by('dia_semana')


class HorarioAtencionCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = HorarioAtencion
    template_name = 'attention/horario_atencion/form.html'
    form_class = HorarioAtencionForm
    success_url = reverse_lazy('attention:horario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = 'Crear Horario de Atención'
        context['grabar'] = 'Crear Horario'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        horario = self.object
        save_audit(self.request, horario, action='A')
        messages.success(self.request, f"Éxito al crear el horario para el día {horario.dia_semana}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))


class HorarioAtencionUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = HorarioAtencion
    template_name = 'attention/horario_atencion/form.html'
    form_class = HorarioAtencionForm
    success_url = reverse_lazy('attention:horario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = 'Actualizar Horario de Atención'
        context['grabar'] = 'Actualizar Horario'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        horario = self.object
        save_audit(self.request, horario, action='M')
        messages.success(self.request, f"Éxito al actualizar el horario para el día {horario.dia_semana}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))


class HorarioAtencionDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = HorarioAtencion
    template_name = 'attention/horario_atencion/delete_confirm.html'
    success_url = reverse_lazy('attention:horario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description'] = f"¿Desea eliminar el horario del día {self.object.dia_semana}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f"Éxito al eliminar el horario del día {self.object.dia_semana}.")
        return super().delete(request, *args, **kwargs)


class HorarioAtencionDetailView(LoginRequiredMixin, DetailView):
    model = HorarioAtencion

    def get(self, request, *args, **kwargs):
        horario = self.get_object()
        data = {
            'id': horario.id,
            'dia_semana': horario.dia_semana,
            'hora_inicio': horario.hora_inicio.strftime('%H:%M:%S'),
            'hora_fin': horario.hora_fin.strftime('%H:%M:%S'),
            'Intervalo_desde': horario.Intervalo_desde.strftime('%H:%M:%S'),
            'Intervalo_hasta': horario.Intervalo_hasta.strftime('%H:%M:%S'),
            'activo': horario.activo,
        }
        return JsonResponse(data)
