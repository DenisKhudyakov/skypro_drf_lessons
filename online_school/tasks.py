from celery import shared_task
from django.core.mail import send_mail

from config import settings
from online_school.models import Course, Subscription


@shared_task
def sending_mails(pk):
    course = Course.objects.get(pk=pk)
    subscribers = Subscription.objects.filter(course=pk)

    send_mail(
        subject=f'Курс {course} обновлен',
        message=f'Курс {course} на который вы подписаны обновлен',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscribers.user.email],
    )