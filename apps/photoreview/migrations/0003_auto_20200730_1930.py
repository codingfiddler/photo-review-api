# Generated by Django 3.0.7 on 2020-07-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoreview', '0002_auto_20200730_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedphoto',
            name='username',
            field=models.CharField(default=1, max_length=150),
        ),
    ]