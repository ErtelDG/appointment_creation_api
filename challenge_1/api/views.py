from django.http import HttpResponse
from rest_framework import permissions,  viewsets
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer
from .models import Doctor, Appointment,Patient

# ViewSets define the view behavior.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    #permission_classes = [permissions.IsAuthenticated]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    #permission_classes = [permissions.IsAuthenticated]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")