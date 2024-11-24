from django import forms
from aplication.core.models import Especialidad

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ["nombre", "descripcion", "activo"]

        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el nombre de la especialidad",
            }),
            "descripcion": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ingrese una descripción",
                "rows": 2,
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }

        labels = {
            "nombre": "Nombre de la Especialidad",
            "descripcion": "Descripción",
            "activo": "Activo",
        }