from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'Teacher: {self.user.username}'


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')

    def __str__(self):
        return f'Student: {self.user.username}'
