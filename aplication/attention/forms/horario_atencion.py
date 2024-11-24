from django.forms import ModelForm
from django import forms
from aplication.attention.models import HorarioAtencion

class HorarioAtencionForm(ModelForm):
    class Meta:
        model = HorarioAtencion
        fields = "__all__"

        widgets = {
            "dia_semana": forms.Select(attrs={
                "class": "form-select shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "id": "id_dia_semana",
            }),
            "hora_inicio": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "id": "id_hora_inicio",
            }),
            "hora_fin": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "id": "id_hora_fin",
            }),
            "Intervalo_desde": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "id": "id_intervalo_desde",
            }),
            "Intervalo_hasta": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "id": "id_intervalo_hasta",
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "id": "id_activo",
            }),
        }

        labels = {
            "dia_semana": "Día de la Semana",
            "hora_inicio": "Hora de Inicio",
            "hora_fin": "Hora de Fin",
            "Intervalo_desde": "Intervalo Desde",
            "Intervalo_hasta": "Intervalo Hasta",
            "activo": "Activo",
        }