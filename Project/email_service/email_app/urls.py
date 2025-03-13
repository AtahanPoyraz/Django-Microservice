from django.urls import path
from .views import *

urlpatterns = [
    path('send-verify/<str:jwt>', SendVerifyEmailView.as_view(), name="send_verify_email"),
    path('send-password-reset/<str:jwt>', SendPasswordResetView.as_view(), name="send_password_reset_email")
]