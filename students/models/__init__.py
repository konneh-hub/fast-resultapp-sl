"""
Students app models
"""
from django.db import models
from django.contrib.auth.models import User
from core.mixins import TimestampMixin, AuditMixin
from core.constants import STUDENT_STATUS_CHOICES
from universities.models import University, Campus, AcademicYear
from academics.models import Program


class StudentProfile(AuditMixin):
    """Extended student profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=20, unique=True)
    university = models.ForeignKey(University, on_delete=models.PROTECT, related_name='students')
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
    )
    phone_number = models.CharField(max_length=20)
    status = models.CharField(
        max_length=20,
        choices=STUDENT_STATUS_CHOICES,
        default='active'
    )
    is_international = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['student_id']
    
    def __str__(self):
        return f"{self.student_id} - {self.user.get_full_name()}"


class StudentEnrollment(AuditMixin):
    """Student enrollment in a program for a semester"""
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='enrollments')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    semester = models.ForeignKey('universities.Semester', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    total_credits = models.IntegerField(default=0)
    is_registered = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('student', 'academic_year', 'semester')
        ordering = ['-academic_year', '-semester']
    
    def __str__(self):
        return f"{self.student.student_id} - {self.academic_year.year}"


class EnrolledCourse(TimestampMixin):
    """Individual course enrollment"""
    enrollment = models.ForeignKey(StudentEnrollment, on_delete=models.CASCADE, related_name='courses')
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    is_retake = models.BooleanField(default=False)
    previous_grade = models.CharField(max_length=10, blank=True, null=True)
    
    class Meta:
        unique_together = ('enrollment', 'course')
    
    def __str__(self):
        return f"{self.enrollment.student.student_id} - {self.course.code}"


class StudentDocument(TimestampMixin):
    """Student documents (certificates, etc.)"""
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(
        max_length=50,
        choices=[
            ('admission', 'Admission Letter'),
            ('transcript', 'Transcript'),
            ('certificate', 'Certificate'),
            ('other', 'Other'),
        ]
    )
    file = models.FileField(upload_to='student_documents/%Y/%m/%d/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.student.student_id} - {self.document_type}"
