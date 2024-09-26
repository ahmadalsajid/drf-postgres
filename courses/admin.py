from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("name", "teacher")


admin.site.register(Course, CourseAdmin)
