from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from online_school.models import Course, Lesson, Subscription, Payments
from online_school.paginators import CoursePaginator, LessonPaginator
from online_school.permissions import IsModerator, IsOwnerOrStaff
from online_school.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer, PaymentsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course model"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]
        elif self.action == "create":
            self.permission_classes = [IsOwnerOrStaff]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания Lesson"""

    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


class LessonListAPIViewSet(generics.ListAPIView):
    """Класс для получения списка Lesson"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    pagination_class = LessonPaginator


class LessonDetailAPIViewSet(generics.RetrieveAPIView):
    """Класс для просмотра Lesson"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


class LessonUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    """Класс для обновления Lesson"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


class LessonDeleteAPIViewSet(generics.RetrieveDestroyAPIView):
    """Класс для удаления Lesson"""

    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


class CourseCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания Course"""

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class CourseUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    """Класс для обновления Course"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff | IsModerator]  # TODO IsOwnerOrStaff


class SubscriptionCreateAPIView(APIView):
    """Контроллер создания и удаление подписки"""
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user  = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка успешно удалена"
        else:
            subs_item = Subscription(user=user, course=course_item) # Создание подписки
            subs_item.save()
            message  =  "Подписка успешно создана"
        return Response({"message": message})

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