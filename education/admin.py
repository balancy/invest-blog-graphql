  
from django.contrib import admin

from education.models import (
    Category,
    Course,
    Lesson,
    Mentor,
    Schedule,
    Student,
    Tag
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "title"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "title", "responsible", "category"
    raw_id_fields = "responsible", "category"


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = "id", "title", "mentor", "course"
    raw_id_fields = "mentor", "course", "tags"


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status"
    raw_id_fields = "user",


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = "id", "student", "lesson", "lesson_time"
    raw_id_fields = "student", "lesson"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status"
    raw_id_fields = "user",


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "id", "title"