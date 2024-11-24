from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Doctor

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "nombres", "apellidos", "cedula", "fecha_nacimiento", "direccion",
            "latitud", "longitud", "codigoUnicoDoctor", "especialidad",
            "telefonos", "email", "horario_atencion", "duracion_cita", 
            "curriculum", "firmaDigital", "foto", "imagen_receta", "activo"
        ]
        error_messages = {
            "cedula": {
                "unique": "Ya existe un doctor con esta cédula.",
            },
            "email": {
                "unique": "Ya existe un doctor con este correo electrónico.",
            },
        }
        widgets = {
            "nombres": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombres",
                    "id": "id_nombres",
                    "class": "form-control",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese apellidos",
                    "id": "id_apellidos",
                    "class": "form-control",
                }
            ),
            "cedula": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese cédula",
                    "id": "id_cedula",
                    "class": "form-control",
                }
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "Ingrese fecha de nacimiento",
                    "id": "id_fecha_nacimiento",
                    "class": "form-control",
                }
            ),
            "direccion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese dirección de trabajo",
                    "id": "id_direccion",
                    "class": "form-control",
                }
            ),
            "latitud": forms.NumberInput(
                attrs={
                    "placeholder": "Latitud",
                    "id": "id_latitud",
                    "class": "form-control",
                }
            ),
            "longitud": forms.NumberInput(
                attrs={
                    "placeholder": "Longitud",
                    "id": "id_longitud",
                    "class": "form-control",
                }
            ),
            "codigoUnicoDoctor": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese código único",
                    "id": "id_codigoUnicoDoctor",
                    "class": "form-control",
                }
            ),
            "especialidad": forms.SelectMultiple(
                attrs={
                    "id": "id_especialidad",
                    "class": "form-select",
                }
            ),
            "telefonos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese teléfono(s)",
                    "id": "id_telefonos",
                    "class": "form-control",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Ingrese correo electrónico",
                    "id": "id_email",
                    "class": "form-control",
                }
            ),
            "horario_atencion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese horario de atención",
                    "id": "id_horario_atencion",
                    "class": "form-control",
                }
            ),
            "duracion_cita": forms.NumberInput(
                attrs={
                    "placeholder": "Duración en minutos",
                    "id": "id_duracion_cita",
                    "class": "form-control",
                }
            ),
            "curriculum": forms.FileInput(
                attrs={
                    "id": "id_curriculum",
                    "class": "form-control",
                }
            ),
            "firmaDigital": forms.FileInput(
                attrs={
                    "id": "id_firmaDigital",
                    "class": "form-control",
                }
            ),
            "foto": forms.FileInput(
                attrs={
                    "id": "id_foto",
                    "class": "form-control",
                }
            ),
            "imagen_receta": forms.FileInput(
                attrs={
                    "id": "id_imagen_receta",
                    "class": "form-control",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "form-check-input",
                }
            ),
        }

    # Validación personalizada para nombres
    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres")
        if not nombres or len(nombres) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombres.upper()

    # Validación personalizada para apellidos
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos")
        if not apellidos or len(apellidos) < 2:
            raise ValidationError("El apellido debe tener al menos 2 caracteres.")
        return apellidos.upper()
from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Doctor

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "nombres", "apellidos", "cedula", "fecha_nacimiento", "direccion",
            "latitud", "longitud", "codigoUnicoDoctor", "especialidad",
            "telefonos", "email", "horario_atencion", "duracion_cita", 
            "curriculum", "firmaDigital", "foto", "imagen_receta", "activo"
        ]
        error_messages = {
            "cedula": {
                "unique": "Ya existe un doctor con esta cédula.",
            },
            "email": {
                "unique": "Ya existe un doctor con este correo electrónico.",
            },
        }
        widgets = {
            "nombres": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombres",
                    "id": "id_nombres",
                    "class": "form-control",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese apellidos",
                    "id": "id_apellidos",
                    "class": "form-control",
                }
            ),
            "cedula": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese cédula",
                    "id": "id_cedula",
                    "class": "form-control",
                }
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "Ingrese fecha de nacimiento",
                    "id": "id_fecha_nacimiento",
                    "class": "form-control",
                }
            ),
            "direccion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese dirección de trabajo",
                    "id": "id_direccion",
                    "class": "form-control",
                }
            ),
            "latitud": forms.NumberInput(
                attrs={
                    "placeholder": "Latitud",
                    "id": "id_latitud",
                    "class": "form-control",
                }
            ),
            "longitud": forms.NumberInput(
                attrs={
                    "placeholder": "Longitud",
                    "id": "id_longitud",
                    "class": "form-control",
                }
            ),
            "codigoUnicoDoctor": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese código único",
                    "id": "id_codigoUnicoDoctor",
                    "class": "form-control",
                }
            ),
            "especialidad": forms.SelectMultiple(
                attrs={
                    "id": "id_especialidad",
                    "class": "form-select",
                }
            ),
            "telefonos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese teléfono(s)",
                    "id": "id_telefonos",
                    "class": "form-control",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Ingrese correo electrónico",
                    "id": "id_email",
                    "class": "form-control",
                }
            ),
            "horario_atencion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese horario de atención",
                    "id": "id_horario_atencion",
                    "class": "form-control",
                }
            ),
            "duracion_cita": forms.NumberInput(
                attrs={
                    "placeholder": "Duración en minutos",
                    "id": "id_duracion_cita",
                    "class": "form-control",
                }
            ),
            "curriculum": forms.FileInput(
                attrs={
                    "id": "id_curriculum",
                    "class": "form-control",
                }
            ),
            "firmaDigital": forms.FileInput(
                attrs={
                    "id": "id_firmaDigital",
                    "class": "form-control",
                }
            ),
            "foto": forms.FileInput(
                attrs={
                    "id": "id_foto",
                    "class": "form-control",
                }
            ),
            "imagen_receta": forms.FileInput(
                attrs={
                    "id": "id_imagen_receta",
                    "class": "form-control",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "form-check-input",
                }
            ),
        }

    # Validación personalizada para nombres
    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres")
        if not nombres or len(nombres) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombres.upper()

    # Validación personalizada para apellidos
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos")
        if not apellidos or len(apellidos) < 2:
            raise ValidationError("El apellido debe tener al menos 2 caracteres.")
        return apellidos.upper()
