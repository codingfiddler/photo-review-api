from rest_framework import serializers
from .models import CustomUser, UploadedPhoto
from django import forms

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class CustomUserSerializer(serializers.ModelSerializer):
    profile_image = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "username", "location", "bio", "profile_image"]

class UploadedPhotoSerializer(serializers.ModelSerializer):

    photo = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = UploadedPhoto
        fields = "__all__"

    def create(self, validated_data):
        return UploadedPhoto.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.email = validated_data.get('email', instance.email)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.username = validated_data.get('username', instance.username)
        instance.title = validated_data.get('title', instance.title)
        instance.location_taken = validated_data.get('location_taken', instance.location_taken)
        instance.photo_id = validated_data.get('photo_id', instance.photo_id)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.taken_date = validated_data.get('taken_date', instance.taken_date)
        instance.uploaded_date = validated_data.get('uploaded_date', instance.uploaded_date)
        instance.software_used = validated_data.get('software_used', instance.software_used)
        instance.camera_used = validated_data.get('camera_used', instance.mcamera_usedail)
        instance.camera_lens = validated_data.get('camera_lens', instance.camera_lens)
        instance.aperture = validated_data.get('aperture', instance.aperture)
        instance.shutter_speed = validated_data.get('shutter_speed', instance.shutter_speed)
        instance.iso = validated_data.get('iso', instance.iso)

        instance.save()
        print(instance)
        return instance

