from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError("Username didn't come!")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, username, password=None, **extra_fields):
        if not password:
            raise TypeError("Password did not come!")
        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
gender = (
    (0, 'Male'),
    (1, 'Famale'),
)

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=225, unique=True, db_index=True)
    full_name = models.CharField(max_length=225, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    date_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True, null=True, blank=True)
    gender = models.IntegerField(choices=gender, default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_created =models.DateField(auto_now_add=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIREMENTS_FIELD  = []

    def __str__(self):
        if self.full_name:
            return f'{self.full_name}'
        return f'{self.username}'

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    


    

