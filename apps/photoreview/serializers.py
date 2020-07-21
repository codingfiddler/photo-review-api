from rest_framework import serializers
from apps.photoreview.models import MinecraftWorld, Animal


class MinecraftWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinecraftWorld
        # We only want to display the below fields when returning data
        # You can still send any of the hidden fields in payloads
        fields = [
            'name',
            'id'
        ]


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        # All fields will be shown
        fields = '__all__'
