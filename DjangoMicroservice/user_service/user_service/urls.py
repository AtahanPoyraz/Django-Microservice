from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="User Service API",
        default_version='v1',
        description="API Documentation for user service",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="atahanpoyraz@gmail.com"),
        license=openapi.License(name="GNU GPLv3"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('user-app/', include('user_app.urls')),  
]
