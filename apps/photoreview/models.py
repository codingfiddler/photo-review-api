from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django import forms

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
    title = models.CharField(max_length = 100)
    photo = models.ImageField()
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length = 200, null=True)
    location_taken = models.CharField(max_length = 500, help_text="Earth, Orion Arm")
    photo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    taken_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    uploaded_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    software_used = models.TextField(max_length = 1000, blank=True, null=True)
    camera_used = models.CharField(max_length = 100, blank= True, null=True)
    camera_lens = models.CharField(max_length = 100, blank= True, null=True)
    aperture = models.CharField(max_length = 100, blank= True, null=True)
    shutter_speed = models.IntegerField(blank=True, null=True)
    iso = models.CharField(max_length=100, blank=True, null=True)


    # exif = ExifField(
    #     source='image',
    # )


    # def get_exif(filename):
    #     image = Image.open(filename)
    #     # image.verify()
    #     return image._getexif()
    # exif = get_exif(photo)

    # exif = ExifField(
    #     source='photo',
    #     denormalized_fields={
    #         'camera': exifgetter('Model'),
    #     },
    # )

# class AllImages(models.Model):
    