from django.shortcuts import render
from apps.photoreview.serializers import StormTrooperSerializer
from apps.photoreview.models import StormTrooper
from rest_framework import viewsets

# Create your views here.
class StormTrooperViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StormTrooperSerializer
    queryset = StormTrooper.objects.all()
