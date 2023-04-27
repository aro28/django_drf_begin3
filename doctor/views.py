from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializers import DoctorSerializers, PatientSerializers
from . models import Doctor, Patient

# class DoctorListCreateViewAPIView(generics.ListCreateAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializers
# через класс
class PatientListCreateViewAPIview(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

# через функцию
@api_view(http_method_names=['POST', 'GET'])
def doctor_list_create_api_view(request):

    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializers(instance=doctors, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        received_data = request.data
        serializer = DoctorSerializers(data=received_data)  #Here the data is provided in JSON format while composing the HTTP request.
        if serializer.is_valid():
            doctor = serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

@api_view(http_method_names=['POST', 'GET', 'DELETE'])
def doctor_delete_view(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializers(instance=doctors, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        received_data = request.data
        serializer = DoctorSerializers(data=received_data)  #Here the data is provided in JSON format while composing the HTTP request.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=204)