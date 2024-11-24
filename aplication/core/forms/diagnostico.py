from django.forms import ModelForm, ValidationError
from django import forms

from aplication.core.models import Diagnostico

# Definición de la clase DiagnosticoForm que hereda de ModelForm
class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
        # Campos que se muestran en este orden en el formulario
        fields = ["codigo", "descripcion", "datos_adicionales", "activo"]

        # Mensajes de error personalizados para ciertos campos
        error_messages = {
            "codigo": {
                "unique": "El código ingresado ya existe.",
            },
        }

        # Personalización de los widgets del formulario
        widgets = {
            "codigo": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el código del diagnóstico",
                    "id": "id_codigo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "descripcion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese la descripción del diagnóstico",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "datos_adicionales": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese datos adicionales (opcional)",
                    "id": "id_datos_adicionales",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                    "rows": 4,
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }