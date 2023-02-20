from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Doctor, Appointment, Patient

# Serializers define the API representation.
class DoctorSerializer(serializers.HyperlinkedModelSerializer):
  
  def getUserDetails(self, obj):
        userDetailsJSON = {'username': obj.user.username}
        return userDetailsJSON

  user_detail = serializers.SerializerMethodField("getUserDetails")
  
  class Meta:
    model = Doctor
    fields = ['id', 'is_doctor', 'user_detail', 'speciality','title']



class PatientSerializer(serializers.HyperlinkedModelSerializer):
  
  def getUserDetails(self, obj):
        userDetailsJSON = {'username': obj.user.username}
        return userDetailsJSON

  user_detail = serializers.SerializerMethodField("getUserDetails")
  
  class Meta:
    model = Patient
    fields = ['id', 'user_detail', 'is_patient']



class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
  
  
  class Meta:
    model = Appointment
    fields = ['id', 'title', 'description','patient', 'doctor', 'date', 'created_at']