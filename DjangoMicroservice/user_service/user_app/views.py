from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserModelSerializer, CreateUserSerializer, UpdateUserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser 

class AuthBasedAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperUser]

class GetUsers(APIView):
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
    def get(self, request, user_id, format=None):
        user = get_object_or_404(UserModel, pk=user_id)
        serializer = UserModelSerializer(user)
        return Response(
            {
                "data": serializer.data,
                "message": "User retrieved successfully",
                "code": status.HTTP_200_OK
            },
            status=status.HTTP_200_OK,
        )

class CreateUser(APIView):    
    @swagger_auto_schema(
        request_body=CreateUserSerializer,
        responses={
            201: "User created successfully",
            400: "Validation error occurred",
        },
    )
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
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
    @swagger_auto_schema(
        request_body=UpdateUserSerializer,
        responses={
            200: "User updated successfully",
            400: "Validation error occurred",
        },
    )
    def put(self, request, user_id, format=None):
        user = get_object_or_404(UserModel, pk=user_id)
        serializer = UpdateUserSerializer(user, data=request.data, partial=True)
        
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

class DeleteUserById(APIView):
    def delete(self, request, user_id, format=None):
        user = get_object_or_404(UserModel, pk=user_id)
        user.delete()
        return Response(
            {
                "data": None,
                "message": "User deleted successfully",
                "code": status.HTTP_204_NO_CONTENT
            },
            status=status.HTTP_204_NO_CONTENT,
        )