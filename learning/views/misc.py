from rest_framework import viewsets, permissions
from learning.models.misc import Progress, Enrollment
from learning.permission import IsOwnerOrReadOnly
from learning.serializers.misc import ProgressSerializer, EnrollmentSerializer, EnrollmentCreateSerializer, \
    ProgressCreateSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return EnrollmentCreateSerializer
        return EnrollmentSerializer

    def perform_create(self, serializer):
        # Agar student userdan olinishi kerak bo'lsa, shu yerda set qilamiz
        serializer.save()


class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProgressCreateSerializer
        return ProgressSerializer

    def perform_create(self, serializer):
        serializer.save()
