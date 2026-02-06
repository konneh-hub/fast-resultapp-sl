"""
Django admin configuration for lecturers app
"""
from django.contrib import admin
from lecturers.models import LecturerProfile, LecturerQualification


@admin.register(LecturerProfile)
class LecturerProfileAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'user', 'university', 'department', 'title', 'is_active')
    list_filter = ('title', 'is_active', 'university')
    search_fields = ('staff_id', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(LecturerQualification)
class LecturerQualificationAdmin(admin.ModelAdmin):
    list_display = ('lecturer', 'qualification_type', 'field_of_study', 'year_obtained')
    list_filter = ('qualification_type', 'year_obtained')
