from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True, max_length = 200)
    location = models.CharField(max_length = 200, blank=True)
    bio = models.TextField(max_length = 500, blank=True, help_text='Write something cool!')
    profile_image = models.ImageField(default='apps/photoreview/default.jpeg')
    

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = []


class UploadedPhoto(models.Model):
    photo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 100)
    photo = models.ImageField()
