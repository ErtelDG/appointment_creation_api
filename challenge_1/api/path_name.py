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