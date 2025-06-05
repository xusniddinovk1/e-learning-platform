from rest_framework import serializers
from learning.models import Lesson, Course
from learning.serializers import TeacherProfileSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'video_url']


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    teacher = TeacherProfileSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'created_at', 'lessons']
