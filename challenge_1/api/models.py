
import datetime
from django.db import models
from django.contrib.auth.models import User


TITLE_CHOICES = [
  ('Dr.', 'Dr.'),
  ('Prof. Dr.', 'Prof. Dr.'),
  ('Dr. rer. nat', 'Dr. rer. nat.')
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
    title = models.CharField(max_length=50, default="No title"),
    description = models.CharField(max_length=100, default="No description")
    patient = models.OneToOneField(Patient,on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.today())
    created_at = models.DateTimeField(auto_created=datetime.datetime.today(), default=datetime.datetime.today())