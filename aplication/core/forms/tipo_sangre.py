from django.forms import ModelForm
from django import forms
from aplication.core.models import TipoSangre

class TipoSangreForm(ModelForm):
    class Meta:
        model = TipoSangre
        fields = ["tipo", "descripcion"]
        widgets = {
            "tipo": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese tipo de sangre",
                    "class": "form-control",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese una descripción",
                    "class": "form-control",
                    "rows": 3,
                }
            ),
        }
        labels = {
            "tipo": "Tipo de Sangre",
            "descripcion": "Descripción",
        }