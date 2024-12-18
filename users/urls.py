# from django.contrib.auth.views import LoginView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserProfileAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
    RegisterView,
    LoginView
)

app_name = UsersConfig.name

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("profile/<int:pk>/", UserProfileAPIView.as_view(), name="profile"),
    path("update/", UserUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="delete"),
]
