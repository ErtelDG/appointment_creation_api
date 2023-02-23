from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import path_name


urlpatterns = [
    path('users', path_name.user_list, name='user-list'),
    path('users/<int:pk>', path_name.user_detail, name='user-detail'),
    path('doctors', path_name.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>', path_name.doctor_detail, name='doctor_detail'),
    path('patients', path_name.patient_list, name='patient_list'),
    path('patients/<int:pk>', path_name.patient_detail, name='patient_detail'),
    path('appointments', path_name.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>', path_name.appointment_detail, name='appointment_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)