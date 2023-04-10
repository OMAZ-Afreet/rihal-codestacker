from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import MinLengthValidator


class User(AbstractUser):
    REQUIRED_FIELDS = []
    
    password = models.CharField(max_length=128, validators=[])
    
    def __str__(self):
        return self.username