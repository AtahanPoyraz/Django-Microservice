from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .tasks import verify_email_task, reset_password_email_task
from .serializers import SendEmailSerializer

from drf_yasg.utils import swagger_auto_schema

class SendVerifyEmailView(APIView):
    @swagger_auto_schema(
        request_body=SendEmailSerializer,
        responses={201: SendEmailSerializer}
    )
    def post(self, request, jwt):
        serializer = SendEmailSerializer(data=request.data)
        
        if serializer.is_valid():
            to = serializer.validated_data["to"]
            subject = serializer.validated_data["subject"]

            result = verify_email_task.apply_async(args=[to, subject, jwt]).get()
            
            if "status_code" not in result:
                return Response({"error": result.get("error", "Unknown error")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if result["status_code"] in [200, 202]:
                return Response({"status": result["status_code"], "message": result.get("message", "Email sended successfully")}, status=status.HTTP_200_OK)

            return Response({"error": result.get("error", "An error occurred")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"status": status.HTTP_400_BAD_REQUEST, "error": "Missing or invalid data!"}, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetView(APIView):
    @swagger_auto_schema(
        request_body=SendEmailSerializer,
        responses={201: SendEmailSerializer}
    )
    def post(self, request, jwt):
        serializer = SendEmailSerializer(data=request.data)
        
        if serializer.is_valid():
            to = serializer.validated_data["to"]
            subject = serializer.validated_data["subject"]

            result = reset_password_email_task.apply_async(args=[to, subject, jwt]).get()
            
            if "status_code" not in result:
                return Response({"error": result.get("error", "Unknown error")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if result["status_code"] in [200, 202]:
                return Response({"status": result["status_code"], "message": result.get("message", "Email sended successfully")}, status=status.HTTP_200_OK)

            return Response({"error": result.get("error", "An error occurred")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"status": status.HTTP_400_BAD_REQUEST, "error": "Missing or invalid data!"}, status=status.HTTP_400_BAD_REQUEST)
