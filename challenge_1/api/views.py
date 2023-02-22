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


@api_view (['GET', 'POST'])
def DoctorViewSet(request):
    if request.method == "GET":
        doctors = models.Doctor.objects.all()
        doctors_serializer = serializers.DoctorSerializer(doctors, many=True)
        return JsonResponse(doctors_serializer.data, safe=False)
    
    elif request.method == 'POST':
        new_doctor_data = JSONParser().parse(request)
        user = User.objects.filter(pk = new_doctor_data['user'])
        print(user.count)
        if ( user.count == 0 ):
            return JsonResponse({'message':'user not exists'}, status=status.HTTP_400_BAD_REQUEST)
        new_doctor_serializer = serializers.DoctorSerializer(data=new_doctor_data)
        if new_doctor_serializer.is_valid():
            new_doctor_serializer.save()
            return JsonResponse(new_doctor_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(new_doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




#class DoctorViewSet(APIView):
#    permission_classes = [permissions.IsAuthenticated]
#       try:
#       doctor_instance = models.Doctor.objects.get(pk = self.request.data['pk'])
#   except models.Doctor.DoesNotExist:
#       return JsonResponse({'message':'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
#              
#   def get(self, request, format=None):
#       queryset = models.Doctor.objects.all()
#       serializer = serializers.DoctorSerializer(queryset, many=True)
#       return Response(serializer.data)
#   
#   def post (self, request, format=None):
#       serializer = serializers.DoctorSerializer(data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
#   
#   def put(self, request, format=None):
#       
#           
#       serializer = serializers.DoctorSerializer(doctor_instance, data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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