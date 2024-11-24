from django.views.generic import TemplateView

from aplication.attention.models import Atencion, CitaMedica
from aplication.core.models import Paciente
from datetime import date, datetime

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         # Obtener la fecha y hora actual
        now = datetime.now()
        proximas_citas = (
            CitaMedica.objects.filter(fecha__gte=now.date())
            .exclude(fecha=now.date(), hora_cita__lt=now.time())  # Excluye las citas pasadas del mismo día
            .order_by('fecha', 'hora_cita')[:3]  # Limita a las 3 primeras
        )
       
        context.update({
            "title": "SaludSync",
            "title1": "Sistema Medico",
            "title2": "Sistema Medico",
            "can_paci": Paciente.cantidad_pacientes(),  # Total de pacientes
            "can_cit": CitaMedica.cantidad_citas_por_dia(date.today()),  # Citas de hoy
            "proximas_citas": proximas_citas,
        })
        print(context["can_paci"], context["can_cit"])  # Para verificar en la consola
        return context
   