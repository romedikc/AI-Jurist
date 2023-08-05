from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import User
from apps.users.serializers import (
    RegisterUserSerializer,
    LoginUserSerializer,

)


class RegisterUserView(CreateAPIView):
    """Register employee view"""

    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()


class LoginUserView(CreateAPIView):
    """User login view"""

    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed("Пользователь не найден!")

        if not user.check_password(password):
            raise AuthenticationFailed("Неверный пароль!")

        refresh = RefreshToken.for_user(user)

        response_data = {
            "detail": "Вы успешно авторизовались!",
            "user_id": str(user.id),
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(data=response_data, status=status.HTTP_200_OK)
