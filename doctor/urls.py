from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.doctor_list_create_api_view),
    path('patient/', views.PatientListCreateViewAPIview.as_view()),
    path('doctor/<int:pk>/', views.doctor_delete_view, name = 'doctor_delete'),
]