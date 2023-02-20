from django.urls import path, include
from rest_framework import routers
from .views import DoctorViewSet, PatientViewSet, AppointmentViewSet

from . import views

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]