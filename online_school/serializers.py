from rest_framework import serializers

from online_school.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for Lessons"""

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for the Course model"""

    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True, source="lesson_set")

    class Meta:
        model = Course
        fields = ['title', 'description', 'count_lessons', 'lessons']

    @staticmethod
    def get_count_lessons(obj):
        return Lesson.objects.filter(course=obj).count()




