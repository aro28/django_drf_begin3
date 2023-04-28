from rest_framework import serializers

from .models import Doctor, Patient

class DoctorSerializers(serializers.Serializer): #отвечает за сериализацию (то есть, за преобразование в формат JSON и обратно) объектов класса Doctor:
    f_name = serializers.CharField() #декларируемое, класс поля и его атрибут мы задаем самостоятельно
    work_exp = serializers.IntegerField()

    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)
        #
        # return Doctor.objects.create(
        #     f_name = validated_data['f_name'],
        #     work_exp = validated_data['work_exp'],
        # )

    def update(self, instance, validated_data):
        instance.f_name, instance.work_exp = validated_data['f_name'], validated_data.get('work_exp')
        instance.save()
        return instance
class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'f_name', 'purpose_visit', 'doctor']   # Поля id, f_name, purpose_visit и doctor — автоматически создаваемые.
