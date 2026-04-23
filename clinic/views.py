from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Anyone can register!
    serializer_class = RegisterSerializer
from rest_framework import viewsets, permissions
from .models import Doctor, Patient, PatientDoctorMapping
from .serializers import DoctorSerializer, PatientSerializer, PatientDoctorMappingSerializer

# View for Doctor Management
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated] # Only logged-in users [cite: 40, 45]

# View for Patient Management
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return patients created by the person logged in 
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the 'created_by' field to the current user 
        serializer.save(created_by=self.request.user)

# View for Mapping Doctors to Patients
class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated] 