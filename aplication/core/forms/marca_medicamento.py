from django import forms
from django.forms import ModelForm
from aplication.core.models import MarcaMedicamento

class MarcaMedicamentoForm(ModelForm):
    class Meta:
        model = MarcaMedicamento
        fields = ["nombre", "descripcion", "activo"]

        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el nombre de la marca",
                    "class": "form-control",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese una descripción (opcional)",
                    "class": "form-control",
                    "rows": 3,
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }
