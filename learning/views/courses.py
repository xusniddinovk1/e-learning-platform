from learning.models.courses import Course, Lesson
from learning.serializers.courses import CourseSerializer, LessonSerializer
from rest_framework import viewsets
from learning.permission import IsStaffOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
