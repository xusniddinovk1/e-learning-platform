from learning.models import Course, Lesson
from learning.serializers import CourseSerializer, LessonSerializer
from rest_framework import viewsets
from learning.permissions import IsStaffOrReadOnly



class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer