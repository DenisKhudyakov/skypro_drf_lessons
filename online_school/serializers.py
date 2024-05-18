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
    lessons = LessonSerializer(many=True)
    read_only = True

    class Meta:
        model = Course
        fields = ['title', 'description', 'count_lessons', 'lessons']

    @staticmethod
    def get_count_lessons(obj):
        return Lesson.objects.filter(course=obj).count()

    def create(self, validated_data):
        """Явный метод для создания объекта"""
        lessons = validated_data.pop('lessons')
        course = Course.objects.create(**validated_data)
        for lesson in lessons:
            Lesson.objects.create(course=course, **lesson)
        return course

