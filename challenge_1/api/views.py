from django.http import Http404
from . import serializers
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User

 


# ViewSets define the view behavior.
class DoctorViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]  
    def get(self, request, format=None):
        queryset = models.Doctor.objects.all()
        serializer = serializers.DoctorSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = serializers.DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


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
   

class UsersViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        all_users = User.objects.all().values('id','username', 'first_name', 'last_name', 'email')
        user_list = list(all_users)
        serializer = serializers.UsersSerializer(user_list, many=True)
        return Response(serializer.data)
        