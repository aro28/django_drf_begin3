from rest_framework import serializers

from .models import Doctor, Patient

class DoctorSerializers(serializers.Serializer): #отвечает за сериализацию (то есть, за преобразование в формат JSON и обратно) объектов класса Doctor:
    f_name = serializers.CharField(allow_blank=True) #декларируемое, класс поля и его атрибут мы задаем самостоятельно
    work_exp = serializers.IntegerField()

    def validate_f_name(self, value):
        excluded_chars = "●!#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~"
        for char in value:
            if char in excluded_chars:
                raise serializers.ValidationError(f"Символ {[char]} запрещен в имени. ")

    def create(self, validated_data):
        # return Doctor.objects.create(**validated_data)
        # #
        return Doctor.objects.create(
            f_name = validated_data['f_name'],
            work_exp = validated_data['work_exp'],
        )

    def update(self, instance, validated_data):
        instance.f_name, instance.work_exp = validated_data.get('f_name', 'work_exp')
        instance.save()
        return instance
class PatientSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(allow_blank=True) #декларируемое, класс поля и его атрибут мы задаем самостоятельно

    class Meta:
        model = Patient
        fields = ['id', 'f_name', 'purpose_visit', 'doctor']   # Поля id, f_name, purpose_visit и doctor — автоматически создаваемые.
