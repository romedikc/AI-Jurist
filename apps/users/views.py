from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import User
from apps.users.serializers import (
    UserSerializer,
    LoginUserSerializer,

)


class UserView(ModelViewSet):
    """Register user view"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_type', 'specialization']

    def perform_create(self, serializer):
        serializer.save(user_type='client')


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
