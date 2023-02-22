from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import path_name


urlpatterns = [
    #path('doctors', views.DoctorViewSet),
    #path('patients', views.PatientViewSet.as_view()),
    #path('appointments', views.AppointmentViewSet.as_view()),
    path('users/', path_name.user_list, name='user-list'),
    path('users/<int:pk>/', path_name.user_detail, name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)