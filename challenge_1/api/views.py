from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from . import serializers
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from datetime import datetime

class DoctorViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = models.Doctor.objects.all()
        serializer = serializers.DoctorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Erstelle zunächst einen neuen User
        user_serializer = serializers.UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
        # Erstelle dann den neuen Doctor mit dem User als ForeignKey
        doctor_serializer = serializers.DoctorSerializer(data=request.data)
        if doctor_serializer.is_valid():
            doctor_serializer.save(user=user)
            return Response(doctor_serializer.data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = models.Doctor.objects.all()
        doctor = queryset.filter(id=pk).first()
        if doctor:
            serializer = serializers.DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        doctor = models.Doctor.objects.filter(id=pk).first()
        if not doctor:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        doctor = models.Doctor.objects.filter(id=pk).first()
        if not doctor:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        doctor_name = doctor.user.username
        doctor.delete()
        return Response({'message':'user deleted successully', 'doctor':doctor_name},status=status.HTTP_200_OK)


class PatientViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = models.Patient.objects.all()
        serializer = serializers.PatientSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Erstelle zunächst einen neuen User
        user_serializer = serializers.UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
        # Erstelle dann den neuen Doctor mit dem User als ForeignKey
        patient_serializer = serializers.PatientSerializer(data=request.data)
        if patient_serializer.is_valid():
            patient_serializer.save(user=user)
            return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = models.Patient.objects.all()
        patient = queryset.filter(id=pk).first()
        if patient:
            serializer = serializers.PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        patient = models.Patient.objects.filter(id=pk).first()
        if not patient:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        patient = models.Patient.objects.filter(id=pk).first()
        if not patient:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        patient_name = patient.user.username
        patient.delete()
        return Response({'message':'user deleted successully', 'doctor':patient_name},status=status.HTTP_200_OK)


class AppointmentViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AppointmentSerializer
    queryset = models.Appointment.objects.all()

    def list(self, request):
        queryset = models.Appointment.objects.all()
        serializer = serializers.AppointmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        required_fields = ['title', 'description', 'patient', 'doctor', 'date']

      
        for field in required_fields:
            if field not in request.data:
                error_message = f"{field} is required."
                raise ParseError(detail=error_message)
        
        try:
            patient = models.Patient.objects.get(id=request.data['patient'])
        except ObjectDoesNotExist:
            patients = list(models.Patient.objects.values_list('id', flat=True))
            error_message = f"Invalid patient ID. Available IDs: {patients}"
            raise ValidationError(detail=error_message)

        try:
            doctor = models.Doctor.objects.get(id=request.data['doctor'])
        except ObjectDoesNotExist:
            doctors = list(models.Doctor.objects.values_list('id', flat=True))
            error_message = f"Invalid doctor ID. Available IDs: {doctors}"
            raise ValidationError(detail=error_message)
                

        try:
            datetime.strptime(str(request.data['date']), '%Y-%m-%dT%H:%M')
        except ValueError:
            error_message = 'Invalid date format. Must be YYYY-MM-DDThh:mm:ss'
            raise ValidationError(detail=error_message)
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            appointment = serializer.save(doctor=doctor, patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        try:
            appointment = models.Appointment.objects.get(pk=pk)
        except models.Appointment.DoesNotExist:
            return Response({'error': 'appointment not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            appointment = models.Appointment.objects.get(pk=pk)
        except models.Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            appointment = models.Appointment.objects.get(pk=pk)
        except models.Appointment.DoesNotExist:
            return Response({'error': 'appointment not found'}, status=status.HTTP_404_NOT_FOUND)
        appointment_title = appointment.title
        appointment.delete()
        return Response({'message':'appointment deleted successully', 'apponintment':appointment_title},status=status.HTTP_200_OK)
   

class UsersViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = User.objects.all()
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_CREATED)

    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message':'user deleted successully'},status=status.HTTP_200_OK)