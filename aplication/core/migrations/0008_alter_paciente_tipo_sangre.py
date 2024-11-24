# Generated by Django 4.2.16 on 2024-11-16 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_tipocategoria_categoria_examen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='tipo_sangre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tipos_sangre', to='core.tiposangre', verbose_name='Tipo de Sangre'),
        ),
    ]
