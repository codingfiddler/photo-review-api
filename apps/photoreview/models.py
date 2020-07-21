from django.db import models


class MinecraftWorld(models.Model):
    seed = models.CharField(max_length=200)
    name = models.CharField(max_length=500)


class Animal(models.Model):
    legs = models.IntegerField()

    PIG = 'pig'
    OX = 'ox'
    HORSE = 'horse'
    VALID_TYPE_OPTIONS = [
        (PIG, 'Pig'),
        (OX, 'Ox'),
        (HORSE, 'Horse'),
    ]
    animal_type = models.CharField(
        choices=VALID_TYPE_OPTIONS,
        max_length=10
    )
    # Animals can only have one world, but a world can have many animals
    world = models.ForeignKey(MinecraftWorld, on_delete=models.CASCADE)
