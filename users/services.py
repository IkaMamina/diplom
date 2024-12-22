import secrets
import string

from pprint import pprint
import random

from smsaero import SmsAero, SmsAeroException

from config.settings import SMSAERO_EMAIL, SMSAERO_API_KEY
from users.models import User


# def generate_code():
#     """Создаем случайный код"""
#
#     kod = string.digits
#     while True:
#         random_code = "".join(secrets.choice(kod) for i in range(6))
#         if (
#             any(c.islower() for c in random_code)
#             and any(c.isupper() for c in random_code)
#             and sum(c.isdigit() for c in random_code) >= 3
#         ):
#             break
#     print(random_code)
#     return random_code


def create_invite_code():
    """Проверяем инвайт код на уникальность, для реферальной системы"""

    alphabet = string.ascii_lowercase + string.digits
    invite_code = ''.join(random.choices(alphabet, k=6))
    return invite_code

    # invite_code = generate_code()
    #
    # while invite_code in [code.invite_code for code in User.objects.all()]:
    #     invite_code = generate_code()
    #
    # return invite_code


def send(phone: int, message: str) -> dict:
    """phone (int): Номер телефона, на который будет отправлено SMS-сообщение.
    message (str): Содержимое SMS-сообщения, которое будет отправлено.
    """
    api = SmsAero(SMSAERO_EMAIL, SMSAERO_API_KEY)

    return api.send_sms(phone, message)


# if __name__ == '__main__':
#     try:
#         result = send(70000000000, 'Hello, World!')
#         pprint(result)
#     except SmsAeroException as e:
#         print(f"An error occurred: {e}")
