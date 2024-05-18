from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentsListAPIView(ListAPIView):
    """Контроллер списка платежей"""
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)  # Набор полей для
    ordering_fields = ('data_payment',)  # сортировки