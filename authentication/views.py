# authentication/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomPasswordResetForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationForm

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('user_login')

class UserRegistrationView(FormView):
    template_name = 'authentication/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomPasswordResetView(PasswordResetView):
    template_name = 'authentication/password_reset.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('user_login')
