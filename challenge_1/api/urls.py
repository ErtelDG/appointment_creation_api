from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('doctors', views.DoctorViewSet),
    path('patients', views.PatientViewSet.as_view()),
    path('appointments', views.AppointmentViewSet.as_view()),
    path('users', views.UsersViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)