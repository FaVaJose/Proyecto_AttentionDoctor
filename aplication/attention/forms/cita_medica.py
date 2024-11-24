from django.forms import ModelForm
from django import forms
from aplication.attention.models import CitaMedica

class CitaMedicaForm(ModelForm):
    class Meta:
        model = CitaMedica
        fields = '__all__'  # Incluir todos los campos del modelo
        widgets = {
            'paciente': forms.Select(attrs={
                'class': 'form-select shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'id': 'id_paciente',
            }),
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'id': 'id_fecha',
            }),
            'hora_cita': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'id': 'id_hora_cita',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'id': 'id_estado',
            }),
        }
        labels = {
            'paciente': 'Paciente',
            'fecha': 'Fecha de la Cita',
            'hora_cita': 'Hora de la Cita',
            'estado': 'Estado de la Cita',
        }
