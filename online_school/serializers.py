from rest_framework import serializers

from online_school.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for the Course model"""
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for Lessons"""
    class Meta:
        model = Lesson
        fields = '__all__'