from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learning.views import (
    TeacherProfileViewSet,
    StudentProfileViewSet,
    CourseViewSet,
    LessonViewSet,
    EnrollmentViewSet,
    ProgressViewSet
)

router = DefaultRouter()
router.register(r'teachers', TeacherProfileViewSet, basename='teacher')
router.register(r'students', StudentProfileViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'progresses', ProgressViewSet, basename='progress')

urlpatterns = [
    path('', include(router.urls)),
]
