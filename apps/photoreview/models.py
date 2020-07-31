from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import datetime
from django.conf import settings
from django import forms
# from comments.models import Comment

# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length = 150)
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True, max_length = 200)
    location = models.CharField(max_length = 200, blank=True)
    bio = models.TextField(max_length = 500, blank=True, help_text='Write something cool!')
    profile_image = models.ImageField(default='apps/photoreview/default.jpeg', null=True)
    

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = []

class Tag(models.Model):
    tag = models.CharField(max_length=200, blank=True)

class UploadedPhoto(models.Model):
    title = models.CharField(max_length = 100)
    photo = models.ImageField()
    username = models.CharField(max_length=150, default=1)
    # username = models.ForeignKey(CustomUser, blank=True, null=True, default=1, on_delete=models.CASCADE, related_name='portfolio')
    location_taken = models.CharField(max_length = 500, help_text="Earth, Orion Arm")
    photo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    created_at = models.DateTimeField(auto_now=True, editable=False)
    taken_date = forms.DateField(required=False)
    uploaded_date = forms.DateField(initial=datetime.date.today)

    software_used = models.TextField(max_length = 1000, blank=True, null=True)
    camera_used = models.CharField(max_length = 100, blank= True, null=True)
    camera_lens = models.CharField(max_length = 100, blank= True, null=True)
    aperture = models.CharField(max_length = 100, blank= True, null=True)
    shutter_speed = models.CharField(max_length=50, blank=True, null=True)
    iso = models.CharField(max_length=100, blank=True, null=True)

    tags = models.ManyToManyField(Tag,)

class Comment(models.Model):
    photo_id = models.ForeignKey(UploadedPhoto, related_name='comments', on_delete=models.CASCADE)
    user_comment = models.TextField(max_length=500, help_text="Praise / Constructive Feedback")
    date_posted = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(CustomUser, related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post) 
