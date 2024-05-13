from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""

    name = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта', max_length=255)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', unique=True)
    city = models.CharField(max_length=50, verbose_name='Город')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"