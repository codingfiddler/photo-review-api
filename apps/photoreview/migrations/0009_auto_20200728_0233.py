# Generated by Django 3.0.7 on 2020-07-28 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoreview', '0008_auto_20200728_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedphoto',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]