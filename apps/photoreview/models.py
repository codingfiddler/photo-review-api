from django.db import models

# Create your models here.
class StormTrooper(models.Model):
    name = models.CharField(
        default='TK-421',
        max_length=100
    )
    location = models.CharField(
        default='Death Star',
        max_length=200

    )
    SHORT = 'short'
    TALL = 'tall'
    VALID_HEIGHT_OPTIONS = [
        (SHORT, 'Short'),
        (TALL, 'Tall'),
    ]
    height = models.CharField(
        choices=VALID_HEIGHT_OPTIONS,
        max_length=20
    )
