from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import viewsets
from apps.photoreview.models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .forms import CustomUserCreationForm

class SignUpViewSet(viewsets.ViewSet):
    def checkToken(self, request):
        username = request.data["username"]
        password = request.data["password"]
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, username=username)
        if user.check_password(password):
            return Response({"status": "okay"})
    
