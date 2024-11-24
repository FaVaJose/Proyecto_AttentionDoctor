from django import forms
from django.forms import ModelForm
from aplication.core.models import Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = [
            "nombres",
            "apellidos",
            "cedula",
            "fecha_nacimiento",
            "cargo",
            "sueldo",
            "direccion",
            "latitud",
            "longitud",
            "foto",
            "activo",
        ]
        widgets = {
            "nombres": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombres"}),
            "apellidos": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese apellidos"}),
            "cedula": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese cédula"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "cargo": forms.Select(attrs={"class": "form-control"}),
            "sueldo": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese sueldo"}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese dirección"}),
            "latitud": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Latitud"}),
            "longitud": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Longitud"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }