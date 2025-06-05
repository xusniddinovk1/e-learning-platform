from rest_framework import viewsets
from learning.models import TeacherProfile, StudentProfile
from learning.serializers import TeacherProfileSerializer, StudentProfileSerializer
from rest_framework import permissions


class TeacherProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudentProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
