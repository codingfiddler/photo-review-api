# Generated by Django 3.0.7 on 2020-07-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoreview', '0005_auto_20200730_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='uploadedphoto',
            name='tags',
        ),
    ]
