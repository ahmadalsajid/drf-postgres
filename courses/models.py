from django.db import models
from users.models import Student, Teacher


class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    students = models.ManyToManyField(Student, related_name='courses')
    exam_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Courses'
        ordering = ('-created_at',)
