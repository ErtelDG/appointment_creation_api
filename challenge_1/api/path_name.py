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