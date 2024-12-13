from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm, Form, CharField

from users.models import User


class UserRegisterForm(ModelForm):
    """Форма регистрации"""

    class Meta:
        model = User
        fields = ("phone",)


class SmsCode(Form):
    """Форма кода"""

    code = CharField(label="Код из СМС")


class UserUpdateForm(UserChangeForm):
    """Форма обновления данных пользователя"""

    def _clean_ref_code(self):
        """Проверка ref_code"""

        ref_code = self.cleaned_data.get("ref_code")
        if self.instance.ref_code:
            raise forms.ValidationError("Вы уже использовали код")
        if not ref_code:
            return ref_code
        if ref_code == self.instance.invite_code:
            raise forms.ValidationError("Вы не можете использовать свой же код")
        if not User.objects.filter(invite_code=ref_code).exists():
            raise forms.ValidationError("Пригласительный код не найден")
        return ref_code

    class Meta:
        model = User
        fields = ("phone", "ref_code",)
