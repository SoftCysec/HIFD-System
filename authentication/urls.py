# authentication/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('register/', views.UserRegistrationView.as_view(), name='user_registration'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
]
