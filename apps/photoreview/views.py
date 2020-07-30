from apps.photoreview.models import CustomUser, UploadedPhoto

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status, filters, generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.filters import SearchFilter, OrderingFilter

from .forms import CustomUserCreationForm, UpdateUserInformationForm
from .serializers import CustomUserSerializer, UploadedPhotoSerializer
import boto3

class LoginViewSet(viewsets.ViewSet):
    def checkToken(self, request):
        username = request.data["username"]
        password = request.data["password"]

        try:
            queryset = CustomUser.objects.filter(username=username, password=password)
            resultsList = list(queryset)
            if len(resultsList) != 0:
                user = resultsList[0]
                if user:
                    print(user)
                    print('hello')
                    token = Token.objects.create(user=user)
                    return Response({"status": "okay", "token":token.key})
            else:
                return Response({"status": "go away"}, status=401)

        except Exception as e:
            print(e)
            return Response({"status": "something is wrong"})

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

class SignUpViewSet(viewsets.ViewSet, APIView):
    def userInfo(self, request):
        full_name = request.data["full_name"]
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        location = request.data["location"]
        bio = request.data["bio"]
        profile_image = request.data["profile_image"]

        username_queryset = CustomUser.objects.filter(username=username)
        email_queryset = CustomUser.objects.filter(email=email)

        if username_queryset.exists():
            return Response({"status": "username taken"})
        if email_queryset.exists():
            return Response({"status":"email already in use"})

        parser_class = (FileUploadParser,)

        def post(self, request, *args, **kwargs):

            file_serializer = CustomUser(data=request.data['profile_image'])

            if file_serializer.is_valid():
                file_serializer.save()
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        customUser = CustomUser.objects.create(
            full_name = full_name,
            username=username,
            email=email,
            password=password,
            location=location,
            bio=bio,
            profile_image=profile_image
        )

        data = CustomUserSerializer(instance = customUser).data

        return Response(data, status=201)

class UploadedPhotoViewSet(viewsets.ModelViewSet):
    queryset=UploadedPhoto.objects.all()
    serializer_class = UploadedPhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']   

class SearchImagesViewSet(generics.ListAPIView):
    queryset = UploadedPhoto.objects.all()
    serializer_class = UploadedPhotoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'camera_used', 'location_taken', 'software_used']

class EditCustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UpView(APIView):
    def get(self, request):
        return Response("ok", status=200)
