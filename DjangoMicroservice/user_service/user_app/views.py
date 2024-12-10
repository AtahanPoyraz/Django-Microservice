from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserModelSerializer, CreateUserDTO, UpdateUserDTO
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]  

class GetUsers(APIView):
    permission_classes = [IsAuthenticated, IsSuperUser]

    def get(self, request, format=None):
        users = UserModel.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(
            {
                "data": serializer.data,
                "message": "Users retrieved successfully",
                "code": status.HTTP_200_OK

            },
            status=status.HTTP_200_OK,
        )

class GetUsersById(APIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    
    def get(self, request, user_id, format=None):
        try:
            user = UserModel.objects.get(pk=user_id)
            serializer = UserModelSerializer(user)
            return Response(
                {
                    "data": serializer.data,
                    "message": "User retrieved successfully",
                    "code": status.HTTP_200_OK
                },
                status=status.HTTP_200_OK,
            )
        except UserModel.DoesNotExist:
            return Response(
                {
                    "data": None,
                    "message": "User not found",
                    "code": status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        
class CreateUser(APIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    
    @swagger_auto_schema(
        request_body=CreateUserDTO,
        responses={
            201: "User created successfully",
            400: "Validation error occurred",
        },
    )
    def post(self, request, format=None):
        serializer = CreateUserDTO(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            
            return Response(
                {
                    "data": {
                        "id": user.id,
                        "email": user.email,
                    },
                    "message": "User created successfully",
                    "code": status.HTTP_201_CREATED
                },
                status=status.HTTP_201_CREATED,
            )
        
        return Response(
            {
                "data": None,
                "message": "Validation error occurred",
                "errors": serializer.errors,
                "code": status.HTTP_400_BAD_REQUEST

            },
            status=status.HTTP_400_BAD_REQUEST,
        )

class UpdateUserById(APIView):
    permission_classes = [IsAuthenticated, IsSuperUser]

    @swagger_auto_schema(
        request_body=UpdateUserDTO,
        responses={
            200: "User updated successfully",
            400: "Validation error occurred",
        },
    )
    def put(self, request, user_id, format=None):
        try:
            user = UserModel.objects.get(pk=user_id)
            serializer = UpdateUserDTO(user, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "data": serializer.data,
                        "message": "User updated successfully",
                        "code": status.HTTP_200_OK
                    },
                    status=status.HTTP_200_OK,
                )
            
            return Response(
                {
                    "data": None,
                    "message": "Validation error occurred",
                    "errors": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        except UserModel.DoesNotExist:
            return Response(
                {
                    "data": None,
                    "message": "User not found",
                    "code": status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND,
            )

class DeleteUserById(APIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    
    def delete(self, request, user_id, format=None):
        try:
            user = UserModel.objects.get(pk=user_id)
            user.delete()
            return Response(
                {
                    "data": None,
                    "message": "User deleted successfully",
                    "code": status.HTTP_204_NO_CONTENT
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except UserModel.DoesNotExist:
            return Response(
                {
                    "data": None,
                    "message": "User not found",
                    "code": status.HTTP_404_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND,
            )