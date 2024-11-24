from django.urls import path
from aplication.core.views.cargo import CargoCreateView, CargoDeleteView, CargoDetailView, CargoListView, CargoUpdateView
from aplication.core.views.diagnostico import DiagnosticoCreateView, DiagnosticoDeleteView, DiagnosticoDetailView, DiagnosticoListView, DiagnosticoUpdateView
from aplication.core.views.doctor import DoctorCreateView, DoctorDeleteView, DoctorDetailView, DoctorListView, DoctorUpdateView
from aplication.core.views.empleado import EmpleadoCreateView, EmpleadoDeleteView, EmpleadoDetailView, EmpleadoListView, EmpleadoUpdateView
from aplication.core.views.especialidad import EspecialidadCreateView, EspecialidadDeleteView, EspecialidadDetailView, EspecialidadListView, EspecialidadUpdateView
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.marca_medicamento import MarcaMedicamentoCreateView, MarcaMedicamentoDeleteView, MarcaMedicamentoDetailView, MarcaMedicamentoListView, MarcaMedicamentoUpdateView
from aplication.core.views.medicamento import MedicamentoCreateView, MedicamentoDeleteView, MedicamentoDetailView, MedicamentoListView, MedicamentoUpdateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.core.views.tipo_medicamento import TipoMedicamentoCreateView, TipoMedicamentoDeleteView, TipoMedicamentoDetailView, TipoMedicamentoListView, TipoMedicamentoUpdateView
from aplication.core.views.tipo_sangre import TipoSangreCreateView, TipoSangreDeleteView, TipoSangreDetailView, TipoSangreListView, TipoSangreUpdateView
 
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # ruta principal
  path('', HomeTemplateView.as_view(),name='home'),
  # rutas doctores VBF
  # path('doctor_list/', views.doctor_List,name="doctor_list"),
  # path('doctor_create/', views.doctor_create,name="doctor_create"),
  # path('doctor_update/<int:id>/', views.doctor_update,name='doctor_update'),
  # path('doctor_delete/<int:id>/', views.doctor_delete,name='doctor_delete'),
  # rutas doctores VBC
  path('patient_list/',PatientListView.as_view() ,name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(),name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(),name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(),name='patient_detail'),
  path("especialidades/", EspecialidadListView.as_view(), name="especialidad_list"),
  path("especialidades/crear/", EspecialidadCreateView.as_view(), name="especialidad_create"),
  path("especialidades/<int:pk>/editar/", EspecialidadUpdateView.as_view(), name="especialidad_update"),
  path("especialidades/<int:pk>/eliminar/", EspecialidadDeleteView.as_view(), name="especialidad_delete"),
  path("especialidades/<int:pk>/", EspecialidadDetailView.as_view(), name="especialidad_detail"),
  path('tipos-sangre/', TipoSangreListView.as_view(), name='tipo_sangre_list'),
  path('tipos-sangre/crear/', TipoSangreCreateView.as_view(), name='tipo_sangre_create'),
  path('tipos-sangre/<int:pk>/editar/', TipoSangreUpdateView.as_view(), name='tipo_sangre_update'),
  path('tipos-sangre/<int:pk>/eliminar/', TipoSangreDeleteView.as_view(), name='tipo_sangre_delete'),
  path('tipos-sangre/<int:pk>/', TipoSangreDetailView.as_view(), name='tipo_sangre_detail'),
  path('cargos/', CargoListView.as_view(), name='cargo_list'),
  path('cargos/crear/', CargoCreateView.as_view(), name='cargo_create'),
  path('cargos/<int:pk>/editar/', CargoUpdateView.as_view(), name='cargo_update'),
  path('cargos/<int:pk>/eliminar/', CargoDeleteView.as_view(), name='cargo_delete'),
  path('cargos/<int:pk>/', CargoDetailView.as_view(), name='cargo_detail'),
  path('diagnosticos/', DiagnosticoListView.as_view(), name='diagnostico_list'),
  path('diagnosticos/crear/', DiagnosticoCreateView.as_view(), name='diagnostico_create'),
  path('diagnosticos/<int:pk>/editar/', DiagnosticoUpdateView.as_view(), name='diagnostico_update'),
  path('diagnosticos/<int:pk>/eliminar/', DiagnosticoDeleteView.as_view(), name='diagnostico_delete'),
  path('diagnosticos/<int:pk>/detalle/', DiagnosticoDetailView.as_view(), name='diagnostico_detail'),
  path('medicamentos/', MedicamentoListView.as_view(), name='medicamento_list'),
  path('medicamento/nuevo/', MedicamentoCreateView.as_view(), name='medicamento_create'),
  path('medicamento/editar/<int:pk>/', MedicamentoUpdateView.as_view(), name='medicamento_update'),
  path('medicamento/eliminar/<int:pk>/', MedicamentoDeleteView.as_view(), name='medicamento_delete'),
  path('medicamento/detalle/<int:pk>/', MedicamentoDetailView.as_view(), name='medicamento_detail'),
  path('marca_medicamento/', MarcaMedicamentoListView.as_view(), name='marca_medicamento_list'),
  path('marca_medicamento/create/', MarcaMedicamentoCreateView.as_view(), name='marca_medicamento_create'),
  path('marca_medicamento/update/<int:pk>/', MarcaMedicamentoUpdateView.as_view(), name='marca_medicamento_update'),
  path('marca_medicamento/delete/<int:pk>/', MarcaMedicamentoDeleteView.as_view(), name='marca_medicamento_delete'),
  path('marca_medicamento/detail/<int:pk>/', MarcaMedicamentoDetailView.as_view(), name='marca_medicamento_detail'),
  path("tipo_medicamento/", TipoMedicamentoListView.as_view(), name="tipo_medicamento_list"),
  path("tipo_medicamento/create/", TipoMedicamentoCreateView.as_view(), name="tipo_medicamento_create"),
  path("tipo_medicamento/<int:pk>/update/", TipoMedicamentoUpdateView.as_view(), name="tipo_medicamento_update"),
  path("tipo_medicamento/<int:pk>/delete/", TipoMedicamentoDeleteView.as_view(), name="tipo_medicamento_delete"),
  path("tipo_medicamento/<int:pk>/detail/", TipoMedicamentoDetailView.as_view(), name="tipo_medicamento_detail"),
  path("empleados/", EmpleadoListView.as_view(), name="empleado_list"),
  path("empleados/create/", EmpleadoCreateView.as_view(), name="empleado_create"),
  path("empleados_update/<int:pk>/", EmpleadoUpdateView.as_view(), name="empleado_update"),
  path("empleados_delete/<int:pk>/", EmpleadoDeleteView.as_view(), name="empleado_delete"),
  path("empleados_detail/<int:pk>/", EmpleadoDetailView.as_view(), name="empleado_detail"),
  path('doctores/', DoctorListView.as_view(), name='doctor_list'),
  path('doctores/nuevo/', DoctorCreateView.as_view(), name='doctor_create'),
  path('doctores/editar/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
  path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
  path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
]