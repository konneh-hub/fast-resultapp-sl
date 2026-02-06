"""
Django admin configuration for universities app
"""
from django.contrib import admin
from universities.models import (
    University, Campus, AcademicYear, Semester, GradingScale, GradePoint, CreditRules
)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country', 'city', 'is_active', 'created_at')
    list_filter = ('is_active', 'country', 'created_at')
    search_fields = ('name', 'code', 'abbreviation')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'code', 'is_main', 'is_active')
    list_filter = ('is_main', 'is_active', 'university')
    search_fields = ('name', 'code', 'location')


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'university', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'university')
    search_fields = ('year',)


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_year', 'number', 'start_date', 'end_date')
    list_filter = ('academic_year', 'number', 'is_current')


@admin.register(GradingScale)
class GradingScaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'scale_type', 'is_active')
    list_filter = ('scale_type', 'is_active')
    search_fields = ('name',)


@admin.register(GradePoint)
class GradePointAdmin(admin.ModelAdmin):
    list_display = ('grade', 'grading_scale', 'point_value')
    list_filter = ('grading_scale',)


@admin.register(CreditRules)
class CreditRulesAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'minimum_credits_per_semester', 'maximum_credits_per_semester')
    list_filter = ('university',)
