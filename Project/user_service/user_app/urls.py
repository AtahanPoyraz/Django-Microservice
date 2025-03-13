from django.urls import path
from .views import *

urlpatterns = [
    path("get", UserListView.as_view(), name="list_user"),
    path("get/<uuid:id>", UserRetrieveView.as_view(), name="retrieve_user"),
    path("create", UserCreateView.as_view(), name="create_user"),   
    path("delete/<uuid:id>", UserDeleteView.as_view(), name="delete_user"),
    path("update/<uuid:id>", UserUpdateView.as_view(), name="update_user"),
    ]