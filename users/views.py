from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class UserListAPIView(ListAPIView):
    """Контроллер списка пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()  # Список пользователей
    permission_classes = [IsAuthenticated]


class UserDetailAPIView(RetrieveAPIView):
    """Контроллер пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(CreateAPIView):
    """Контроллер создания пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()  # Создание пользователя
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_user = serializer.save(is_active=True)
        new_user.save()


class UserDestroyAPIView(DestroyAPIView):  # Деструктор
    """Класс для удаления пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]  # Доступ только для админов
