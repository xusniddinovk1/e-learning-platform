from learning.models import Course, Lesson
from rest_framework import serializers


class LessonSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
