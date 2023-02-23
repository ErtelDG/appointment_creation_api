from django.shortcuts import get_object_or_404
from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

class DoctorViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]


    """
    > The function takes a request, gets all the doctors from the database, serializes them, and returns
    the serialized data
    
    :param request: The request object
    :return: A list of all the doctors in the database.
    """
    def list(self, request):
        queryset = models.Doctor.objects.all()
        serializer = serializers.DoctorSerializer(queryset, many=True)
        return Response(serializer.data)


    """
    If the user serializer is valid, save the user, then if the doctor serializer is valid, save the
    doctor with the user, otherwise delete the user and return the errors
    
    :param request: The request object
    :return: The response is a tuple of the response data and the status code.
    """
    def create(self, request):
        user_serializer = serializers.UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
        doctor_serializer = serializers.DoctorSerializer(data=request.data)
        if doctor_serializer.is_valid():
            doctor_serializer.save(user=user)
            return Response(doctor_serializer.data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """
    > The function retrieves a doctor from the database and returns it as a JSON object
    
    :param request: The request object
    :param pk: The primary key of the model instance that you want to retrieve
    :return: A list of doctors
    """
    def retrieve(self, request, pk=None):
        queryset = models.Doctor.objects.all()
        doctor = queryset.filter(id=pk).first()
        if doctor:
            serializer = serializers.DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)


    """
    If the doctor exists, update the doctor's information with the new information provided in the
    request
    
    :param request: The request object that was sent to the view
    :param pk: The primary key of the object you want to update
    :return: The response is a JSON object with the following keys:
    """
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


    """
    > The function takes a request and a primary key (pk) as arguments, and returns a response
    
    :param request: The request object
    :param pk: The primary key of the object you want to retrieve
    :return: The response is a dictionary with two keys: message and doctor. The message key has a
    string value of "user deleted successfully" and the doctor key has a string value of the username of
    the doctor that was deleted.
    """
    def destroy(self, request, pk=None):
        doctor = models.Doctor.objects.filter(id=pk).first()
        if not doctor:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        doctor_name = doctor.user.username
        doctor.delete()
        return Response({'message':'user deleted successully', 'doctor':doctor_name},status=status.HTTP_200_OK)


class PatientViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]


    """
    > The function takes a request, gets all the patients from the database, serializes them, and
    returns them as a response
    
    :param request: The request object
    :return: A list of all patients in the database.
    """
    def list(self, request):
        queryset = models.Patient.objects.all()
        serializer = serializers.PatientSerializer(queryset, many=True)
        return Response(serializer.data)


    """
    If the user serializer is valid, save the user, then if the patient serializer is valid, save the
    patient with the user, otherwise delete the user and return the patient serializer errors
    
    :param request: The request object
    :return: The response is a tuple of two elements: the first element is the response body (a string)
    and the second element is the HTTP status code.
    """
    def create(self, request):
        user_serializer = serializers.UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
       
        patient_serializer = serializers.PatientSerializer(data=request.data)
        
        if patient_serializer.is_valid():
            patient_serializer.save(user=user)
            return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """
    > Retrieve a patient by id
    
    :param request: The request object
    :param pk: The primary key of the object you want to retrieve
    :return: A dictionary with a key of 'error' and a value of 'Patient not found'
    """
    def retrieve(self, request, pk=None):
        queryset = models.Patient.objects.all()
        patient = queryset.filter(id=pk).first()
        if patient:
            serializer = serializers.PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)


    """
    We're going to update the patient with the given id with the data in the request
    
    :param request: The request object that was sent to the view
    :param pk: The primary key of the patient you want to update
    :return: The response is a JSON object with the following keys:
    """
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


    """
    > The function takes in a request and a primary key (pk) and deletes the patient with the given pk
    
    :param request: The request object
    :param pk: The primary key of the object you want to retrieve
    :return: The response is a dictionary with two keys: message and doctor.
    """
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


    """
    > The function takes a request, gets all the appointments from the database, serializes them, and
    returns them as a response.
    
    :param request: The request object
    :return: A list of all the appointments in the database.
    """
    def list(self, request):
        queryset = models.Appointment.objects.all()
        serializer = serializers.AppointmentSerializer(queryset, many=True)
        return Response(serializer.data)


    """
    If the required fields are not in the request, raise a ParseError. If the patient or doctor ID is
    invalid, raise a ValidationError. If the date is not in the correct format, raise a ValidationError.
    If the serializer is valid, save the appointment and return the serializer data. Otherwise, return
    the serializer errors
    
    :param request: The request object
    :return: The response is a serialized version of the appointment object.
    """
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


    """
    It tries to get an appointment with the given primary key, and if it doesn't exist, it returns a 404
    error. Otherwise, it returns the appointment
    
    :param request: The request object that is sent to the view
    :param pk: primary key
    :return: The appointment object is being returned.
    """
    def retrieve(self, request, pk=None):
        try:
            appointment = models.Appointment.objects.get(pk=pk)
        except models.Appointment.DoesNotExist:
            return Response({'error': 'appointment not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    """
    We're trying to update an appointment, but if the appointment doesn't exist, we return a 404 error.
    If the appointment does exist, we try to update it with the data from the request. If the data is
    valid, we save the appointment and return a 202 status code. If the data is invalid, we return a 400
    status code
    
    :param request: The request object that is sent to the view
    :param pk: The primary key of the object you want to update
    :return: The serializer.data is being returned.
    """
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


    """
    > The function takes in a request and a primary key (pk) and returns a response
    
    :param request: The request object is used to get information about the request that was made to the
    API
    :param pk: The primary key of the appointment to be deleted
    :return: The response is a dictionary with two keys: message and appointment. The message key has a
    value of appointment deleted successfully and the appointment key has a value of the title of the
    appointment that was deleted.
    """
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

    """
    > The function takes a request, gets all the users from the database, serializes them, and returns
    them as a response
    
    :param request: The request object
    :return: A list of all users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    """
    If the serializer is valid, save the serializer and return a 201 status code. If the serializer is
    not valid, return a 400 status code
    
    :param request: The request object
    :return: The serializer.data is being returned.
    """
    def create(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """
    > This function retrieves a single user from the database and returns it as a JSON object
    
    :param request: The request object
    :param pk: The primary key of the object you want to retrieve
    :return: The serializer.data is being returned.
    """
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_CREATED)


    """
    > The update function takes a request and a primary key (pk) as arguments. It then gets the user
    with the given pk, creates a serializer with the user and the request data, and if the serializer is
    valid, it saves the serializer and returns a 202 Accepted response with the serializer data. If the
    serializer is not valid, it returns a 400 Bad Request response with the serializer errors
    
    :param request: The request object
    :param pk: The primary key of the user you want to update
    :return: The serializer.data is being returned.
    """
    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """
    It takes a request and a primary key, and deletes the user with that primary key
    
    :param request: The request object
    :param pk: The primary key of the object you want to retrieve
    :return: The response is being returned.
    """
    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message':'user deleted successully'},status=status.HTTP_200_OK)