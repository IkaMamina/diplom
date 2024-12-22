from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(phone="81111111111", invite_code="123456")
        user.set_password("111111")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
