from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

<<<<<<< Updated upstream
from .forms import CustomUserCreationForm, CustomUserChangeForm
=======
from .forms import CustomUserChangeForm, CustomUserCreationForm
>>>>>>> Stashed changes
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
<<<<<<< Updated upstream
    list_display = ['email', 'username',]
=======
    list_display = ['username','email']
>>>>>>> Stashed changes

admin.site.register(CustomUser, CustomUserAdmin)