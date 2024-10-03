from rest_framework import serializers
from icecream import ic

from users.models import Teacher, Student
from .models import Course
from users.serializers import StudentSerializer, TeacherSerializer


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        teacher = validated_data.pop('teacher') if 'teacher' in validated_data else None
        students = validated_data.pop('students') if 'students' in validated_data else None
        course = Course.objects.create(**validated_data)
        if teacher:
            course.teacher = teacher
            course.save()
        if students:
            course.students.set(students)
            course.save()
        return course

    def update(self, instance, validated_data):
        teacher = validated_data.pop('teacher') if 'teacher' in validated_data else None
        students = validated_data.pop('students') if 'students' in validated_data else None
        instance = super().update(instance, validated_data)
        if teacher:
            instance.teacher = teacher
            instance.save()
        if students:
            instance.students.set(students)
            instance.save()
        return instance


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
