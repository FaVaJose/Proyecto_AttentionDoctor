from django import forms
from django.forms import ModelForm
from aplication.core.models import TipoMedicamento

class TipoMedicamentoForm(ModelForm):
    class Meta:
        model = TipoMedicamento
        fields = ["nombre", "descripcion", "activo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el nombre del tipo de medicamento"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Ingrese una descripción (opcional)", "rows": 3}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
