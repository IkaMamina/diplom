from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import phone_validator

NULLABLE = {"blank": True, "null": True}

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Email", **NULLABLE)
    phone = models.CharField(
        unique=True,
        max_length=11,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        validators=[phone_validator],
    )
    invite_code = models.CharField(max_length=6, verbose_name="Инвайт код", **NULLABLE)
    ref_code = models.CharField(
        max_length=6, verbose_name="Введенный инвайт код", **NULLABLE
    )

    objects = CustomUserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.phone
