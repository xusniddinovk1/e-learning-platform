from django.db import models
from .profile import TeacherProfile, StudentProfile

class Courses(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    teacher = models.ForeignKey(TeacherProfile, )