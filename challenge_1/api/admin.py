from django.contrib import admin
from api.models import Patient, Doctor, Appointment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)