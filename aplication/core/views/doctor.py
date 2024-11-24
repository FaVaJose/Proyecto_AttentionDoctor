from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.models import Doctor
from aplication.core.forms.doctor import DoctorForm
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit


class DoctorListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "core/doctor/list.html"
    model = Doctor
    context_object_name = 'doctores'
    paginate_by = 10

    def get_queryset(self):
        query = Q()
        search_query = self.request.GET.get('q', None)
        if search_query:
            query |= Q(nombres__icontains=search_query)
            query |= Q(apellidos__icontains=search_query)
            query |= Q(cedula__icontains=search_query)
            query |= Q(codigoUnicoDoctor__icontains=search_query)
        return self.model.objects.filter(query).order_by('apellidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Doctores"
        context['title1'] = "Gestión de Doctores"
        return context


class DoctorCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = Doctor
    template_name = "core/doctor/form.html"
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Doctor"
        context['title1'] = "Registrar Nuevo Doctor"
        context['grabar'] = "Registrar Doctor"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object
        save_audit(self.request, doctor, action='A')
        messages.success(self.request, f"Éxito al registrar al doctor {doctor.nombre_completo}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Por favor, corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))


class DoctorUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = Doctor
    template_name = "core/doctor/form.html"
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Actualizar Doctor"
        context['title1'] = "Editar Información del Doctor"
        context['grabar'] = "Actualizar Doctor"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object
        save_audit(self.request, doctor, action='M')
        messages.success(self.request, f"Éxito al actualizar al doctor {doctor.nombre_completo}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al actualizar el formulario. Por favor, corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))


class DoctorDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Doctor"
        context['grabar'] = "Eliminar Doctor"
        context['description'] = f"¿Desea eliminar al doctor: {self.object.nombre_completo}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar al doctor {self.object.nombre_completo}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)


class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctor

    def get(self, request, *args, **kwargs):
        doctor = self.get_object()
        data = {
            'id': doctor.id,
            'nombres': doctor.nombres,
            'apellidos': doctor.apellidos,
            'foto': doctor.foto.url if doctor.foto else '/static/img/empleado_default.jpg',
            'codigoUnicoDoctor': doctor.codigoUnicoDoctor,
            'especialidad': ", ".join([esp.nombre for esp in doctor.especialidad.all()]),
            'telefonos': doctor.telefonos,
            'email': doctor.email,
            'direccion': doctor.direccion,
            'horario_atencion': doctor.horario_atencion,
            'activo': "Activo" if doctor.activo else "Inactivo",
        }
        return JsonResponse(data)
