# Generated by Django 3.0.7 on 2020-07-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoreview', '0009_auto_20200728_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='full name', max_length=150),
            preserve_default=False,
        ),
    ]