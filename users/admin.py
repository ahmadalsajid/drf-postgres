from django.contrib import admin
from .models import User, Teacher, Student


class UserAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("username", "first_name", "last_name", "email")


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("teacher_id", )
    search_fields = (
        "teacher_id",
    )


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("registration", "user")
    search_fields = (
        "registration",
    )


admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
