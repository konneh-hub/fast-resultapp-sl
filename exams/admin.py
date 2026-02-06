"""
Django admin configuration for exams app
"""
from django.contrib import admin
from exams.models import ExamPeriod, ExamCalendar, ExamRoom, InvigilatorAssignment


@admin.register(ExamPeriod)
class ExamPeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'exam_type', 'start_date', 'end_date', 'is_active')
    list_filter = ('exam_type', 'is_active', 'semester')


@admin.register(ExamCalendar)
class ExamCalendarAdmin(admin.ModelAdmin):
    list_display = ('course', 'exam_period', 'exam_date', 'start_time', 'venue')
    list_filter = ('exam_date', 'exam_period')
    search_fields = ('course__code', 'venue')


@admin.register(ExamRoom)
class ExamRoomAdmin(admin.ModelAdmin):
    list_display = ('room_code', 'campus', 'capacity', 'is_available')
    list_filter = ('is_available', 'campus')
    search_fields = ('room_code', 'location')


@admin.register(InvigilatorAssignment)
class InvigilatorAssignmentAdmin(admin.ModelAdmin):
    list_display = ('exam_calendar', 'lecturer', 'room', 'status')
    list_filter = ('status', 'exam_calendar')
