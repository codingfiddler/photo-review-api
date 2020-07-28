# Generated by Django 3.0.7 on 2020-07-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoreview', '0007_customuser_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedphoto',
            name='aperture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphoto',
            name='camera_lens',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphoto',
            name='camera_used',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphoto',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphoto',
            name='iso',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphoto',
            name='location_taken',
            field=models.CharField(default=0, help_text='Earth, Orion Arm', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadedphoto',
            name='shutter_speed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphoto',
            name='software_used',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphoto',
            name='username',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
