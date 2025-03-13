from django.contrib import admin
from .models import UserModel

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'created_at', 'updated_at')
    search_fields = ('email', 'first_name', 'last_name') 
    list_filter = ('is_active', 'is_staff')  
    ordering = ('created_at',)  

admin.site.register(UserModel, UserModelAdmin)
