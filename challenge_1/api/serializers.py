from rest_framework import serializers
from .models import Doctor, Appointment, Patient
from django.contrib.auth.models import User

# Serializers define the API representation.
class UsersSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email']


class DoctorSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
  class Meta:
    model = Doctor
    fields = ['id', 'user',  'is_doctor', 'speciality','title']



# It creates a serializer for the Patient model.
class PatientSerializer(serializers.ModelSerializer):
  #user = UserSerializer()
  
  class Meta:
    model = Patient
    fields = ['id', 'user', 'is_patient']
    
  
# This class is a serializer for the Appointment model
class AppointmentSerializer(serializers.ModelSerializer):
     
  class Meta:
    model = Appointment
    fields = ['id', 'title', 'description','patient', 'doctor', 'date', 'created_at']