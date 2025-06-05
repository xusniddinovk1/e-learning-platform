from django.db import models
from .profile import StudentProfile
from .profile import TeacherProfile


class Course(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name='courses', blank=True)
    students = models.ManyToManyField(StudentProfile, through='Enrollment', related_name='enrolled_courses',
                                      blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.course.title} - {self.title}'
