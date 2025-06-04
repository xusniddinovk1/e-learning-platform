from learning.models import Course, Lesson
from learning.serializers import CourseSerializer, LessonSerializer
from rest_framework import viewsets
from learning.permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly



class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer