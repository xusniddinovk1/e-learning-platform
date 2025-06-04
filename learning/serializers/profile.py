from learning.models import TeacherProfile, StudentProfile
from rest_framework import serializers


class TeacherProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
