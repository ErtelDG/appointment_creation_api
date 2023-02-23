from api import views

user_list = views.UsersViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = views.UsersViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


doctor_list = views.DoctorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
doctor_detail = views.DoctorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


patient_list = views.PatientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
patient_detail = views.PatientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


appointment_list = views.AppointmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
appointment_detail = views.AppointmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})