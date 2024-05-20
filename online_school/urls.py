from django.urls import path

from online_school.apps import OnlineSchoolConfig
from rest_framework import routers

from online_school.views import (
    LessonCreateAPIViewSet,
    LessonListAPIViewSet,
    LessonDetailAPIViewSet,
    LessonDeleteAPIViewSet,
    LessonUpdateAPIViewSet,
    CourseViewSet,
    CourseCreateAPIViewSet, CourseUpdateAPIViewSet,
)

app_name = OnlineSchoolConfig.name

router = routers.DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")
urlpatterns = [
    path("lessons/create/", LessonCreateAPIViewSet.as_view(), name="lesson-create"),
    path("lessons/list/", LessonListAPIViewSet.as_view(), name="lessons"),
    path("lessons/<int:pk>/", LessonDetailAPIViewSet.as_view(), name="lesson-detail"),
    path(
        "lessons/<int:pk>/delete/",
        LessonDeleteAPIViewSet.as_view(),
        name="lesson-delete",
    ),
    path(
        "lessons/<int:pk>/update/",
        LessonUpdateAPIViewSet.as_view(),
        name="lesson-update",
    ),
    path("course/create/", CourseCreateAPIViewSet.as_view(), name="course-create"),
    path('course/update/<int:pk>/', CourseUpdateAPIViewSet.as_view(), name='course-update'),
] + router.urls
