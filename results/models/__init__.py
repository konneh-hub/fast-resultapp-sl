"""
Results app models - Core engine for result management
"""
from django.db import models
from core.mixins import TimestampMixin, AuditMixin
from core.constants import RESULT_STATUS_CHOICES
from students.models import StudentEnrollment, EnrolledCourse
from academics.models import Course
from universities.models import Semester


class Result(AuditMixin):
    """Main result record"""
    enrollment = models.ForeignKey(StudentEnrollment, on_delete=models.CASCADE, related_name='results')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=RESULT_STATUS_CHOICES,
        default='draft'
    )
    submitted_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    submission_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('enrollment', 'course')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.enrollment.student.student_id} - {self.course.code}"


class ResultComponent(TimestampMixin):
    """Individual result components (CA, Exam, etc.)"""
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='components')
    component_type = models.CharField(
        max_length=50,
        choices=[
            ('assignment', 'Assignment'),
            ('midterm', 'Mid-term Exam'),
            ('final', 'Final Exam'),
            ('practical', 'Practical'),
            ('project', 'Project'),
            ('participation', 'Participation'),
        ]
    )
    max_score = models.FloatField()
    score_obtained = models.FloatField()
    weight = models.FloatField(default=1.0)  # Weighting factor
    
    class Meta:
        unique_together = ('result', 'component_type')
    
    def __str__(self):
        return f"{self.result.course.code} - {self.component_type}"


class Grade(TimestampMixin):
    """Calculated grade from result"""
    result = models.OneToOneField(Result, on_delete=models.CASCADE, related_name='grade')
    total_score = models.FloatField()
    letter_grade = models.CharField(max_length=10)
    grade_point = models.FloatField()
    is_pass = models.BooleanField()
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.result.course.code} - {self.letter_grade}"


class GPARecord(TimestampMixin):
    """Student GPA per semester"""
    enrollment = models.OneToOneField(StudentEnrollment, on_delete=models.CASCADE, related_name='gpa_record')
    semester_gpa = models.FloatField()
    courses_taken = models.IntegerField()
    courses_passed = models.IntegerField()
    total_points = models.FloatField()
    total_credits = models.IntegerField()
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.enrollment.student.student_id} - GPA: {self.semester_gpa}"


class CGPARecord(TimestampMixin):
    """Cumulative GPA record"""
    from students.models import StudentProfile
    
    student = models.OneToOneField('students.StudentProfile', on_delete=models.CASCADE, related_name='cgpa_record')
    cumulative_gpa = models.FloatField()
    total_courses_taken = models.IntegerField()
    total_courses_passed = models.IntegerField()
    total_credits_earned = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-last_updated']
    
    def __str__(self):
        return f"{self.student.student_id} - CGPA: {self.cumulative_gpa}"


class Transcript(AuditMixin):
    """Student transcript"""
    from students.models import StudentProfile
    
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE, related_name='transcripts')
    academic_year = models.ForeignKey(Semester, on_delete=models.CASCADE)
    is_official = models.BooleanField(default=False)
    generated_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='transcripts/%Y/%m/%d/', null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Transcript - {self.student.student_id}"


class ResultLock(AuditMixin):
    """Lock results to prevent unauthorized modifications"""
    enrollment = models.OneToOneField(StudentEnrollment, on_delete=models.CASCADE, related_name='result_lock')
    is_locked = models.BooleanField(default=False)
    locked_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    locked_at = models.DateTimeField(null=True, blank=True)
    unlock_reason = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.enrollment.student.student_id} - {'Locked' if self.is_locked else 'Unlocked'}"


class ResultRelease(AuditMixin):
    """Control result visibility to students"""
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    can_view_results = models.BooleanField(default=False)
    released_date = models.DateTimeField(null=True, blank=True)
    released_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        unique_together = ('semester',)
    
    def __str__(self):
        return f"Release Control - {self.semester.name}"
