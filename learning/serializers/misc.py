from rest_framework import serializers
from learning.models.misc import Enrollment, Progress
from learning.serializers.courses import LessonSerializer, CourseSerializer
from learning.serializers.profile import StudentProfileSerializer


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at']


class EnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']


class ProgressSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Progress
        fields = ['id', 'student', 'lesson', 'completed_at']


class ProgressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['student', 'lesson']
