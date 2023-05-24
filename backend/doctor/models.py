from django.db import models

class Doctor(models.Model):
    f_name = models.CharField(max_length=20)
    work_exp = models.IntegerField()

    def __str__(self):
        return self.f_name
class Patient(models.Model):
    f_name = models.CharField(max_length=20)
    purpose_visit = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.f_name} - {self.purpose_visit} - {self.doctor}'

