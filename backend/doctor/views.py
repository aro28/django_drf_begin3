from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from . serializers import DoctorSerializers, PatientSerializers
from . models import Doctor, Patient
from .my_generic_view import MyGenericListCreateView, MyGenericRetrieveUpdateDestroyView
from rest_framework import viewsets

# CLASS-BASED VIEW
class PatientListCreateViewAPIview(generics.ListCreateAPIView):
    # below comment goes to http://127.0.0.1:8000/swagger/
    """
      Doctor Create and List View
      :params limit: int

      """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers



# CLASS-BASED VIEW inheritated from my generic view
class PatientListCreateView(MyGenericListCreateView): #мы наследуемся от универсального класса(my_generic_view) где находятся POST,GET,DELETE 
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
class PatientRetrieveUpdatDestroyView(MyGenericRetrieveUpdateDestroyView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


#Через функцию
@api_view(http_method_names=['GET', 'POST'])
def doctor_list_create_api_view(request):
    if request.method == 'GET':
        queryset = Doctor.objects.all()
        serializer = DoctorSerializers(queryset, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = DoctorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    # return Response(serializer.data) # ,берет питоновский и возвращает JSON
@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def doctor_retrieve_update_delete_api_view(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'GET':
        serializer = DoctorSerializers(instance=doctor, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = DoctorSerializers(instance=doctor,data=request.data)  #Here the data is provided in JSON format while composing the HTTP request.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=204)


@api_view(http_method_names=['GET', 'POST'])
def patient_list_create_api_view(request):
    if request.method == 'GET':
        queryset = Patient.objects.all()
        serializer = PatientSerializers(queryset, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PatientSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def patient_retrieve_update_delete_api_view(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'GET':
        serializer = PatientSerializers(instance=patient, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = PatientSerializers(instance=patient,data=request.data)  #Here the data is provided in JSON format while composing the HTTP request.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=204)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers