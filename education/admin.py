  
from django.contrib import admin

from education.models import (
    Category,
    Course,
    Mentor,
    Student,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "title"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "title", "category"
    raw_id_fields = "mentors", "category"


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status"
    raw_id_fields = "user",


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status"
    raw_id_fields = "user", "courses"
