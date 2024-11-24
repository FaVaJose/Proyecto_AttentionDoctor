from django.urls import path
from aplication.attention.views.cita_medica import CitaMedicaCreateView, CitaMedicaDeleteView, CitaMedicaDetailView, CitaMedicaListView, CitaMedicaUpdateView
from aplication.attention.views.horario_atencion import HorarioAtencionCreateView, HorarioAtencionDeleteView, HorarioAtencionDetailView, HorarioAtencionListView, HorarioAtencionUpdateView
from aplication.attention.views.medical_attention import AttentionCreateView, AttentionDetailView, AttentionListView, AttentionUpdateView
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
 
app_name='attention' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # rutas de atenciones
  path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
  path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
  path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
  path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
  # path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('horarios/', HorarioAtencionListView.as_view(), name='horario_list'),
  path('horarios_create/', HorarioAtencionCreateView.as_view(), name='horario_create'),
  path('horarios_update/<int:pk>/', HorarioAtencionUpdateView.as_view(), name='horario_update'),
  path('horarios_delete/<int:pk>/', HorarioAtencionDeleteView.as_view(), name='horario_delete'),
  path('horarios_detail/<int:pk>/', HorarioAtencionDetailView.as_view(), name='horario_detail'),
  path("citas/", CitaMedicaListView.as_view(), name="cita_list"),
  path("citas_create/", CitaMedicaCreateView.as_view(), name="cita_create"),
  path("citas_update/<int:pk>/", CitaMedicaUpdateView.as_view(), name="cita_update"),
  path("citas_delete/<int:pk>/", CitaMedicaDeleteView.as_view(), name="cita_delete"),
  path("citas_detail/<int:pk>/", CitaMedicaDetailView.as_view(), name="cita_detail"),
]