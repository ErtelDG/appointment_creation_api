from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime


# A list of tuples. The first element of the tuple is the value that is stored in the database. The
# second element of the tuple is the value that is displayed in the form.
TITLE_CHOICES = [
  ('Dr.', 'Dr.'),
  ('Prof. Dr.', 'Prof. Dr.'),
  ('Dr. rer. nat.', 'Dr. rer. nat.')
]

SPECIALITY_CHOICES = [
  ('Allgemeinmedizin', 'Allgemeinmedizin'),
  ('Hautarzt', 'Hautarzt'),
  ('Radiologie', 'Radiologie')
]


# It creates a new table in the database called Doctor.
class Doctor(models.Model):
    is_doctor = models.BooleanField(default=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50, choices=SPECIALITY_CHOICES)
    title = models.CharField(max_length=50, choices= TITLE_CHOICES)


# It creates a one-to-one relationship between the User model and the Patient model.
class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=True)
      
      
# It creates a class called Appointment. It has a title, description, patient, doctor, date, and
# created_at.
class Appointment(models.Model):
    
    def validate_date(value):
        """
        It takes a datetime object and converts it to a string in the format YYYY-MM-DDThh:mm
        
        :param value: The value that is being validated
        """
        try:
            date_string = str(value.year)+"-"+str(value.month)+"-"+str(value.day)+"T"+str(value.hour)+":"+str(value.minute)
            datetime.strptime(str(date_string), '%Y-%m-%dT%H:%M')
        except ValueError:
            raise ValidationError('Invalid date jjjjjjjjjjjformat. Must be YYYY-MM-DDThh:mm')

  
    title = models.CharField(max_length=50, default="No title")
    description = models.CharField(max_length=100, default="No description")
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.utcnow, validators=[validate_date])
    created_at = models.DateTimeField(auto_created=datetime.now(), default=datetime.now())
    

