from rest_framework import serializers

from users.models import Payments


class PaymentsSerializer(serializers.Serializer):
    """Класс сериализатора для модели Payments"""
    class Meta:
        model = Payments
        fields = '__all__'