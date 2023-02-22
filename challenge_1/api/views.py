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


class PatientViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]  
    def get(self, request, format=None):
        queryset = models.Patient.objects.all()
        serializer = serializers.PatientSerializer(queryset, many=True)
        return Response(serializer.data)


class AppointmentViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]  
    def get(self, request, format=None):
        queryset = models.Appointment.objects.all()
        serializer = serializers.AppointmentSerializer(queryset, many=True)
        return Response(serializer.data)
   

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