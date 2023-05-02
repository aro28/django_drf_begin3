from django.urls import path
from . import views

urlpatterns = [
    path('func/doctor/', views.doctor_list_create_api_view),
    path('func/doctor/<int:pk>', views.doctor_retrieve_update_delete_api_view),

    path('func/patient/', views.patient_list_create_api_view),
    path('func/patient/<int:pk>', views.patient_retrieve_update_delete_api_view),
    path('class/patient/', views.PatientListCreateView.as_view()),
    path('class/patient/<int:pk>', views.PatientRetrieveUpdatDestroyView.as_view()),


]