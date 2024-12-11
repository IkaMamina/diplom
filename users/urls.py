from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserProfileAPIView, UserUpdateAPIView, UserDestroyAPIView, RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserCreateAPIView.as_view(), name="login"),
    path("profile/<int:pk>/", UserProfileAPIView.as_view(), name="profile"),
    path("update/", UserUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="delete"),
]