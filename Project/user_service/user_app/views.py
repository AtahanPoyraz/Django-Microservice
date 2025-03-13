from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import UserModel
from .serializers import UserSerializer
from .permissions import IsSuperUser

from user_app.models import UserModel
from user_app.serializers import UserSerializer

class UserListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    
class UserRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

class UserCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

class UserDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
