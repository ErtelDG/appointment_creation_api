from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime


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


class Doctor(models.Model):
    is_doctor = models.BooleanField(default=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50, choices=SPECIALITY_CHOICES)
    title = models.CharField(max_length=50, choices= TITLE_CHOICES)

class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=True)
      
class Appointment(models.Model):
    def validate_date(value):
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
    

