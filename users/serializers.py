from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Payments, User


class PaymentsSerializer(serializers.Serializer):
    """Класс сериализатора для модели Payments"""

    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели User"""
    class Meta:
        model = User
        fields = "__all__"



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token["username"] = user.username
#         token["email"] = user.email
#         return token
