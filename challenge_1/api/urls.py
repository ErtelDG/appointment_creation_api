from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import path_name
from rest_framework.routers import DefaultRouter
from api import views


urlpatterns = [
    path('users/', path_name.user_list, name='user-list'),
    path('users/<int:pk>/', path_name.user_detail, name='user-detail'),
    path('doctors/', path_name.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', path_name.doctor_detail, name='doctor_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)