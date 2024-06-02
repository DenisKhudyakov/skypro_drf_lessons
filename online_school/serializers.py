from rest_framework import serializers

from online_school.models import Course, Lesson, Payments, Subscription
from online_school.validators import LessonsValidator


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for Lessons"""

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LessonsValidator(url="video_link")]


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for the Course model"""

    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)
    read_only = True

    class Meta:
        model = Course
        fields = ["title", "description", "count_lessons", "lessons"]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    @staticmethod
    def get_count_lessons(obj):
        return Lesson.objects.filter(course=obj).count()

    def create(self, validated_data):
        """Явный метод для создания объекта"""
        lessons = validated_data.pop("lessons")
        course = Course.objects.create(**validated_data)
        for lesson in lessons:
            Lesson.objects.create(course=course, **lesson)
        return course


class SubscriptionSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели Subscription"""

    class Meta:
        model = Subscription
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели Payments"""

    class Meta:
        model = Payments
        fields = "__all__"
