from django.urls import path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('doctor', views.DoctorViewSet)
router.register('patient', views.PatientViewSet)

urlpatterns = [
    path('func/doctor/', views.doctor_list_create_api_view),
    path('func/doctor/<int:pk>', views.doctor_retrieve_update_delete_api_view),

    path('func/patient/', views.patient_list_create_api_view),
    path('func/patient/<int:pk>', views.patient_retrieve_update_delete_api_view),
    path('class/patient/', views.PatientListCreateView.as_view()),
    path('class/patient/<int:pk>', views.PatientRetrieveUpdatDestroyView.as_view()),


]