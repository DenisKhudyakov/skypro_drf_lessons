from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from online_school.models import Course, Lesson
from online_school.permissions import IsOwnerOrStaff, IsModerator
from online_school.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course model"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]
        elif self.action == 'create':
            self.permission_classes = [IsOwnerOrStaff]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIViewSet(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class LessonListAPIViewSet(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]


class LessonDetailAPIViewSet(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]


class LessonUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | IsModerator]


class LessonDeleteAPIViewSet(generics.RetrieveDestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class CourseCreateAPIViewSet(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrStaff]


class CourseUpdateAPIViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff | IsModerator]  # TODO IsOwnerOrStaff
