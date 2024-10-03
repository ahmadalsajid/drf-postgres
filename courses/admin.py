from django.contrib import admin
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
)
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'teacher', 'exam_date')
    search_fields = (
        'name', 'teacher__teacher_id', 'teacher__user__phone',
        'teacher__user__email', 'teacher__user__username',
        'teacher__user__first_name', 'teacher__user__last_name',
        'exam_date'
    )
    list_filter = [
        'teacher',
        # ('students', MultiSelectFieldListFilter)
        ('exam_date', DateRangeFilterBuilder())
    ]


admin.site.register(Course, CourseAdmin)
