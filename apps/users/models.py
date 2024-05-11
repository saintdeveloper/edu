from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from apps.common.models import BaseModel, Address



STATUS = (
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
)
GENDER = (
    (0, "Male"),
    (1, "Famale"),
)

class Account(AbstractUser, BaseModel):
    username = models.CharField(max_length=225, unique=True, db_index=True)
    full_name = models.CharField(max_length=225, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    date_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/',null=True,blank=True)
    email = models.EmailField(unique=True, db_index=True, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    status = models.CharField(choices=STATUS, default='student', max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        if self.full_name:
            return f'{self.full_name}'
        return f'{self.username}'
    
    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }