from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True, max_length = 200)
    location = models.CharField(max_length = 200, blank=True)
    bio = models.TextField(max_length = 500, blank=True, help_text='Write something cool!')
    

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = []