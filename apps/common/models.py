from django.db import models

class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)