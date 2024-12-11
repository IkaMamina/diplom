from rest_framework.exceptions import ValidationError


def phone_validator(phone):
    """Валидация номера телефона"""

    if len(phone) == 11 and (phone[0] == '8' or phone[0] == '7') and phone.isnumeric():
        return True
    else:
        raise ValidationError("Укажите номер телефона в формате 70000000000")