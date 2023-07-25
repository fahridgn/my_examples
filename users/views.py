from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'

class UsersLoginHomeView(LoginView):
    template_name='home.html'
