from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user_list = serializers.SerializerMethodField()

    def get_user_list(self, obj):
        users = User.objects.filter(ref_code=obj.invite_code)
        return [{user.pk, user.phone} for user in users]

    class Meta:
        model = User
        fields = "__all__"
