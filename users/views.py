from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, ProfileSerializer, RegisterSerializer
from users.services import create_invite_code, generate_code


class RegisterView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.invite_code = create_invite_code()
            return Response(user.invite_code, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


class UserCreateAPIView(generics.CreateAPIView):
    """Авторизация пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return_data = {}
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user.invite_code = create_invite_code()
            return_data["invite_code"] = user.invite_code
        except Exception:
            user = User.objects.get(phone=request.data.get("phone"))
            return_data["invite_code"] = user.invite_code
        finally:
            password = generate_code()
            user.set_password(password)
            user.save()

        return Response(return_data, status=status.HTTP_201_CREATED)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновляет данные пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, *args, **kwargs):
        return self.request.user


class UserProfileAPIView(generics.RetrieveAPIView):
    """Возвращает информацию о пользователе"""

    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаляет пользователя"""

    queryset = User.objects.all()
    serializer_class = ProfileSerializer





