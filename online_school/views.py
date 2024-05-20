from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from online_school.models import Course, Lesson
from online_school.permissions import IsModerator, IsOwnerOrStaff
from online_school.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course model"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]
        elif self.action == "create":
            self.permission_classes = [IsOwnerOrStaff]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания Lesson"""

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class LessonListAPIViewSet(generics.ListAPIView):
    """Класс для получения списка Lesson"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]


class LessonDetailAPIViewSet(generics.RetrieveAPIView):
    """Класс для просмотра Lesson"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]


class LessonUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    """Класс для обновления Lesson"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]


class LessonDeleteAPIViewSet(generics.RetrieveDestroyAPIView):
    """Класс для удаления Lesson"""

    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class CourseCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания Course"""

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class CourseUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    """Класс для обновления Course"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff | IsModerator]  # TODO IsOwnerOrStaff
