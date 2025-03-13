from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from .views import *

urlpatterns = [
    path('auth', include('rest_framework.urls')),  
    path("me", MeView.as_view(), name="me"),
    path("sign-up", SignUpView.as_view(), name="sign_up"),
    path('sign-in', jwt_views.TokenObtainPairView.as_view(), name='sign_in'), 
    path('sign-in/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/<str:jwt>', VerifyView.as_view(), name="verify"),
    path('reset-password/<str:jwt>', ResetPasswordView.as_view(), name="reset_password")
]