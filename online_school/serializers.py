from rest_framework import serializers

from online_school.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for the Course model"""

    count_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    @staticmethod
    def get_count_lessons(obj):
        return Lesson.objects.filter(course=obj).count()


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for Lessons"""

    class Meta:
        model = Lesson
        fields = "__all__"
