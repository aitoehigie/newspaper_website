from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ["email", "username", "age", "is_staff", ]
    list_filter = ["email", "username"]

admin.site.register(CustomUser, CustomUserAdmin)
