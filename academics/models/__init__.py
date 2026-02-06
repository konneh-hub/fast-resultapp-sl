"""
Academics app models
"""
from django.db import models
from core.mixins import TimestampMixin, AuditMixin
from universities.models import University, Campus, Semester


class Faculty(AuditMixin):
    """Faculty/School within university"""
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='faculties')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('university', 'code')
        ordering = ['name']
        verbose_name_plural = 'Faculties'
    
    def __str__(self):
        return f"{self.university.code} - {self.name}"


class Department(AuditMixin):
    """Department within a faculty"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('faculty', 'code')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.faculty.university.code} - {self.name}"


class Program(AuditMixin):
    """Academic program/degree"""
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    level = models.CharField(
        max_length=20,
        choices=[
            ('diploma', 'Diploma'),
            ('bachelors', "Bachelor's"),
            ('masters', "Master's"),
            ('phd', 'PhD'),
        ]
    )
    duration_years = models.IntegerField(default=4)
    total_credits = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('department', 'code')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.department.faculty.university.code} - {self.name}"


class Course(AuditMixin):
    """Course/Module offered in a program"""
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    credit_units = models.IntegerField()
    level = models.IntegerField()  # 100, 200, 300, 400, etc.
    is_compulsory = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('program', 'code')
        ordering = ['level', 'name']
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class CourseAllocation(AuditMixin):
    """Allocation of lecturer to course"""
    from lecturers.models import LecturerProfile
    from universities.models import Semester
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='allocations')
    lecturer = models.ForeignKey('lecturers.LecturerProfile', on_delete=models.CASCADE, related_name='course_allocations')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='course_allocations')
    is_coordinator = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('course', 'lecturer', 'semester')
        ordering = ['semester', 'course']
    
    def __str__(self):
        return f"{self.course.code} - {self.lecturer.user.get_full_name()}"
