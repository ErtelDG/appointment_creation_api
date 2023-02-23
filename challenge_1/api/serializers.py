from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor, Patient, Appointment


# It creates a serializer for the User model.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


# The DoctorSerializer class is a subclass of the ModelSerializer class. It has a user field that is a
# read-only UserSerializer. The model is the Doctor model and the fields are the id, user, speciality,
# title, and is_doctor fields
class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'speciality', 'title', 'is_doctor']


# It creates a serializer for the Patient model.
class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'user', 'is_patient']


# It creates a serializer for the Appointment model.
class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'title', 'description', 'patient', 'doctor', 'date', 'created_at']
