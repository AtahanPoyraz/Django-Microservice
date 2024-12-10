from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/users', GetUsers.as_view(), name='get_users'),  
    path('api/v1/users/<uuid:user_id>', GetUsersById.as_view(), name='get_user_by_id'), 
    path('api/v1/users/create', CreateUser.as_view(), name='create_user'),  
    path('api/v1/users/update/<uuid:user_id>', UpdateUserById.as_view(), name='update_user_by_id'),
    path('api/v1/users/delete/<uuid:user_id>', DeleteUserById.as_view(), name='delete_user_by_id'),  
]