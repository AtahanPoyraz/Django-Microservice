from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from .serializers import AuthSerializer
from .permissions import IsActive
from .models import UserModel
import requests

from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class MeView(APIView):
    permission_classes = [IsAuthenticated, IsActive]

    def get(self, request):
        serializer = AuthSerializer(request.user)
        return Response({"user": serializer.data})

class SignUpView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = AuthSerializer

    def generate_verification_token(self, user):
        return str(RefreshToken.for_user(user))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            try:
                response = requests.post(
                    url=f"{settings.API_GATEWAY_INTERNAL_URL}/email/api/v1/send-verify/{self.generate_verification_token(user)}",
                    json={
                        "to":user.email, 
                        "subject":"ACCOUNT VERIFICATON"
                        }
                    )
                if response.status_code == 200:
                    return Response({
                        "status": status.HTTP_201_CREATED,
                        "message": "User created successfully. Verification email sended.",
                        "data": AuthSerializer(user).data
                    }, status=status.HTTP_201_CREATED)
                
                else:
                    return Response({
                        "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                        "message": "Failed to send verification email."
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
            except requests.exceptions.RequestException as e:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": f"An error occurred while sending the verification email: {str(e)}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class VerifyView(APIView):
    def extract_user_from_token(self, jwt):
        token = RefreshToken(jwt)
        return UserModel.objects.get(id=token["user_id"])
    
    def invalidate_token(self, jwt):
        try:
            token = RefreshToken(jwt)
            token.blacklist() 
            
        except Exception as e:
            print(f"Error invalidating token: {str(e)}")

    def post(self, request, jwt):
        try:
            user = self.extract_user_from_token(jwt)
            if not user.is_active:
                user.is_active = True
                user.save()

            self.invalidate_token(jwt)
            return render(request, 'verification-succsess.html', {
                "message": "User successfully verified."
            })

        except UserModel.DoesNotExist:
            return render(request, 'verification-failed.html', {
                "message": "User not found."
            })

        except Exception as e:
            return render(request, 'verification-failed.html', {
                "message": f"An error occurred: {str(e)}"
            })
        
class ResetPasswordView(APIView):
    def extract_user_from_token(self, jwt):
        token = RefreshToken(jwt)
        return UserModel.objects.get(id=token["user_id"])
    
    def invalidate_token(self, jwt):
        try:
            token = RefreshToken(jwt)
            token.blacklist() 

        except Exception as e:
            print(f"Error invalidating token: {str(e)}")
    
    def get(self, request, jwt):
        try:
            self.extract_user_from_token(jwt)
            return render(request, 'reset-password.html', {
                "reset_link": f"{settings.API_GATEWAY_EXTERNAL_URL}/auth/api/v1/reset-password/{jwt}"
            })

        except UserModel.DoesNotExist:
            return render(request, 'something-went-wrong.html', {
                "message": f"An error occurred: {str(e)}"
            })

        except Exception as e:
            return render(request, 'something-went-wrong.html', {
                "message": f"An error occurred: {str(e)}"
            })
        
    def post(self, request, jwt):
        try:
            user = self.extract_user_from_token(jwt)            
            new_password = request.data.get("password")
            confirm_password = request.data.get("confirm_password")

            if not new_password or not confirm_password:
                raise ParseError("Both password fields are required.")

            if new_password != confirm_password:
                raise ParseError("Passwords do not match!")

            validate_password(new_password, user)

            user.password = make_password(new_password)
            user.save()

            self.invalidate_token(jwt)
            return Response({"message": "Password reset successful!"}, status=status.HTTP_200_OK)
        
        except ParseError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
