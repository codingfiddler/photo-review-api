from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UploadedPhoto

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')

# class UpdateUserInformationForm(forms.ModelForm):
#     email = forms.EmailField()
#     profile_image = forms.ImageField()

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'full_name', 'email', 'location', 'bio', 'profile_image']
