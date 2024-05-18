from django.contrib.auth.models import AbstractUser
from django.db import models

from online_school.models import Course, Lesson, NULLABLE


class User(AbstractUser):
    """Модель пользователя"""

    name = None
    email = models.EmailField(
        unique=True, verbose_name="Электронная почта", max_length=255
    )
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", unique=True)
    city = models.CharField(max_length=50, verbose_name="Город")
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    """Модель платежей"""

    PAYMENT_METHODS = (
        ("cash", "Наличными"),
        ("bank", "Банковской картой"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_payment = models.DateTimeField(auto_now_add=True, verbose_name="Дата платежа")
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, **NULLABLE, verbose_name="Оплаченный Курс"
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name="Оплаченный Урок"
    )
    amount = models.FloatField(verbose_name="Сумма платежа")
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        default="bank",
        verbose_name="Способ оплаты",
    )

    def __str__(self):
        return (f"{self.user} - {self.data_payment} - {self.paid_course if self.paid_course else self.paid_lesson} - "
                f"{self.amount}")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ("-data_payment",)
