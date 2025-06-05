from django.db import models

from learning.models.profile import StudentProfile
from learning.models.courses import Course, Lesson


class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'

    def __str__(self):
        return f'{self.student.user.username} enrolled in {self.course.title}'


class Progress(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'lesson')
        verbose_name = 'Lesson Progress'
        verbose_name_plural = 'Progress Records'

    def __str__(self):
        return f'{self.student.user.username} completed {self.lesson.title}'
