from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

class Patient(models.Model):
    # 'created_by' ensures we know which user added this patient [cite: 20]
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class PatientDoctorMapping(models.Model):
    # This connects a patient to a doctor [cite: 31]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents assigning the same doctor to the same patient twice
        unique_together = ('patient', 'doctor')