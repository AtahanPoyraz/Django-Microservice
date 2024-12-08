from django.contrib import admin
from django import forms
from .models import UserModel

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password', 'is_active', 'is_staff', 'is_superuser')

    password = forms.CharField(widget=forms.PasswordInput, required=False)

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    form = UserModelForm

    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')

    ordering = ('-created_at',) 

    list_filter = ('is_active', 'is_staff', 'is_superuser', 'created_at')

    search_fields = ('email', 'username')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password')
        }),
        ('Permissions', {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:  
            obj.set_password(obj.password)  
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset 
        
        return queryset.filter(is_active=True)  
    
    def __str__(self):
        return self.email

