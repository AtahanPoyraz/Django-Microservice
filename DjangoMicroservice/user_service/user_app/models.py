from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password, check_password
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        
        if password:
            user.set_password(password)
        else:
            raise ValueError("Password cannot be empty.")
        
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError("Superusers must have is_staff=True.")
        
        
        if kwargs.get('is_superuser') is not True:
            raise ValueError("Superusers must have is_superuser=True.")

        return self.create_user(email, username, password, **kwargs)

class UserModel(AbstractBaseUser):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField("username", max_length=255, blank=False)
    email = models.EmailField("email", max_length=255, unique=True, blank=False)
    password = models.CharField("password", max_length=128, blank=False)
    is_active = models.BooleanField("is_active", default=True, blank=False)
    is_staff = models.BooleanField("is_staff", default=False, blank=False)
    is_superuser = models.BooleanField("is_superuser", default=False, blank=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
