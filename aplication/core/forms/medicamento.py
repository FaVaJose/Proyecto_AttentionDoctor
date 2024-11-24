from django import forms
from django.forms import ModelForm, ValidationError
from aplication.core.models import Medicamento

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            "tipo", "marca_medicamento", "nombre", "descripcion", 
            "concentracion", "cantidad", "precio", "comercial", "activo"
        ]
        widgets = {
            "tipo": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione el tipo de medicamento",
                }
            ),
            "marca_medicamento": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seleccione la marca del medicamento",
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del medicamento",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese la descripción del medicamento",
                }
            ),
            "concentracion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese la concentración del medicamento",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese la cantidad en stock",
                }
            ),
            "precio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el precio del medicamento",
                }
            ),
            "comercial": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }