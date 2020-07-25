from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import viewsets
from apps.photoreview.models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .forms import CustomUserCreationForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class LoginViewSet(viewsets.ViewSet):
    def checkToken(self, request):
        username = request.data["username"]
        password = request.data["password"]
        try:
            queryset = CustomUser.objects.filter(username=username)
            resultsList = list(queryset)
            if len(resultsList) != 0:
                user = resultsList[0]
                if user:
                    token = Token.objects.create(user=user)
                    return Response({"status": "okay", "token":token.key})
            else:
                return Response({"status": "go away"}, status=401)
            
        except Exception as e:
            print(e)
            return Response({"status": "okay"})

class CheckAuthenticated(viewsets.ViewSet): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def isAuthenticated(self, request):
        return Response({"status": "authenticated"})


class LogoutViewset(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            if user:
                Token.objects.filter(user = user).delete()
                return Response({"status": "going away"})
            else:
                return Response({"status": "oops youre stuck"}, status=401)
            
        except Exception as e:
            print(e)
            return Response({"status": "okay"})