from django.shortcuts import render
from apps.photoreview.serializers import (
    MinecraftWorldSerializer,
    AnimalSerializer
)
from apps.photoreview.models import MinecraftWorld, Animal
from rest_framework import viewsets


# Create your views here.
class MinecraftWorldViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = MinecraftWorldSerializer
    queryset = MinecraftWorld.objects.all()


class AnimalViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
