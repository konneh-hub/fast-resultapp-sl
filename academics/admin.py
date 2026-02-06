"""
Django admin configuration for academics app
"""
from django.contrib import admin
from academics.models import Faculty, Department, Program, Course, CourseAllocation


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'code', 'is_active')
    list_filter = ('is_active', 'university')
    search_fields = ('name', 'code')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'code', 'is_active')
    list_filter = ('is_active', 'faculty')
    search_fields = ('name', 'code')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'code', 'level', 'total_credits')
    list_filter = ('level', 'is_active')
    search_fields = ('name', 'code')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'program', 'credit_units', 'level', 'is_compulsory')
    list_filter = ('level', 'is_compulsory', 'is_active')
    search_fields = ('code', 'name')


@admin.register(CourseAllocation)
class CourseAllocationAdmin(admin.ModelAdmin):
    list_display = ('course', 'lecturer', 'semester', 'is_coordinator')
    list_filter = ('semester', 'is_coordinator')
    search_fields = ('course__code', 'lecturer__staff_id')
