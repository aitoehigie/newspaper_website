from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import CustomUser
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    model = CustomUser
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
