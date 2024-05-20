from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer


class PaymentsListAPIView(ListAPIView):
    """Контроллер списка платежей"""

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # Бэкенд для обработки фильтра
    filterset_fields = (
        "paid_course",
        "paid_lesson",
        "payment_method",
    )  # Набор полей для
    ordering_fields = ("data_payment",)  # сортировки


class UserListAPIView(ListAPIView):
    """Контроллер списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all() # Список пользователей
    permission_classes = [IsAuthenticated]


class UserDetailAPIView(RetrieveAPIView):
    """Контроллер пользователя"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(CreateAPIView):
    """Контроллер создания пользователя"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.is_staff = self.request.user
        new_user.save()


class UserDestroyAPIView(DestroyAPIView): # Деструктор
    """Класс для удаления пользователя"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsAdminUser] # Доступ только для админов


# Ниже просто примеры кода
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer # Сериализатор для токена
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def my_protected_view(request):
#     # Ваш код представления
#     return Response({'message': 'Авторизовано!'})
