from django.db import models


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Address(BaseModel):
    title = models.CharField(max_length=225)
    
    def __str__(self):
        return self.title
    