"""
Django admin configuration for results app
"""
from django.contrib import admin
from results.models import (
    Result, ResultComponent, Grade, GPARecord, CGPARecord, Transcript, ResultLock, ResultRelease
)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'course', 'status', 'submission_date')
    list_filter = ('status', 'submission_date')
    search_fields = ('enrollment__student__student_id', 'course__code')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ResultComponent)
class ResultComponentAdmin(admin.ModelAdmin):
    list_display = ('result', 'component_type', 'max_score', 'score_obtained')
    list_filter = ('component_type',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('result', 'letter_grade', 'grade_point', 'is_pass')
    list_filter = ('is_pass', 'letter_grade')


@admin.register(GPARecord)
class GPARecordAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'semester_gpa', 'courses_passed')
    list_filter = ('created_at',)


@admin.register(CGPARecord)
class CGPARecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'cumulative_gpa', 'total_courses_passed')
    list_filter = ('last_updated',)


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('student', 'academic_year', 'is_official', 'generated_by')
    list_filter = ('is_official', 'created_at')


@admin.register(ResultLock)
class ResultLockAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'is_locked', 'locked_at')
    list_filter = ('is_locked',)


@admin.register(ResultRelease)
class ResultReleaseAdmin(admin.ModelAdmin):
    list_display = ('semester', 'can_view_results', 'released_date')
    list_filter = ('can_view_results',)
