"""
Django admin configuration for students app
"""
from django.contrib import admin
from students.models import StudentProfile, StudentEnrollment, EnrolledCourse, StudentDocument


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'user', 'university', 'program', 'status')
    list_filter = ('status', 'university', 'is_international')
    search_fields = ('student_id', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StudentEnrollment)
class StudentEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'program', 'academic_year', 'semester', 'is_registered')
    list_filter = ('is_registered', 'academic_year', 'semester')
    search_fields = ('student__student_id',)


@admin.register(EnrolledCourse)
class EnrolledCourseAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'course', 'is_retake')
    list_filter = ('is_retake',)
    search_fields = ('course__code',)


@admin.register(StudentDocument)
class StudentDocumentAdmin(admin.ModelAdmin):
    list_display = ('student', 'document_type', 'uploaded_by', 'created_at')
    list_filter = ('document_type', 'created_at')
