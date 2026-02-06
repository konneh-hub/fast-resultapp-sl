"""
Universities app models
"""
from django.db import models
from core.mixins import TimestampMixin, AuditMixin


class University(AuditMixin):
    """Main university model"""
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)
    abbreviation = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Universities'
    
    def __str__(self):
        return f"{self.name} ({self.code})"


class Campus(AuditMixin):
    """Campus/Branch of a university"""
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='campuses')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('university', 'code')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.university.code} - {self.name}"


class AcademicYear(AuditMixin):
    """Academic year definition"""
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='academic_years')
    year = models.CharField(max_length=9)  # e.g., "2023/2024"
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('university', 'year')
        ordering = ['-year']
    
    def __str__(self):
        return f"{self.university.code} - {self.year}"


class Semester(AuditMixin):
    """Semester within an academic year"""
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='semesters')
    name = models.CharField(max_length=50)  # First Semester, Second Semester, Summer
    number = models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Summer')])
    start_date = models.DateField()
    end_date = models.DateField()
    registration_start = models.DateField()
    registration_end = models.DateField()
    exam_start = models.DateField(null=True, blank=True)
    exam_end = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('academic_year', 'number')
        ordering = ['academic_year', 'number']
    
    def __str__(self):
        return f"{self.academic_year.year} - {self.name}"


class GradingScale(AuditMixin):
    """Grading scale definition"""
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='grading_scales')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    scale_type = models.CharField(
        max_length=20,
        choices=[('letter', 'Letter'), ('numeric', 'Numeric'), ('percentage', 'Percentage')]
    )
    min_score = models.FloatField()
    max_score = models.FloatField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('university', 'name', 'scale_type')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.university.code} - {self.name}"


class GradePoint(TimestampMixin):
    """Grade point mapping"""
    grading_scale = models.ForeignKey(GradingScale, on_delete=models.CASCADE, related_name='grade_points')
    grade = models.CharField(max_length=10)  # A, A-, B+, B, etc.
    min_score = models.FloatField()
    max_score = models.FloatField()
    point_value = models.FloatField()  # GPA equivalent
    
    class Meta:
        unique_together = ('grading_scale', 'grade')
        ordering = ['-point_value']
    
    def __str__(self):
        return f"{self.grading_scale.name} - {self.grade} ({self.point_value})"


class CreditRules(AuditMixin):
    """Credit unit rules and requirements"""
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='credit_rules')
    name = models.CharField(max_length=100)
    minimum_credits_per_semester = models.IntegerField(default=12)
    maximum_credits_per_semester = models.IntegerField(default=21)
    minimum_gpa_for_graduation = models.FloatField(default=2.0)
    minimum_gpa_for_good_standing = models.FloatField(default=2.0)
    pass_grade = models.CharField(max_length=10, default='D')
    
    class Meta:
        unique_together = ('university', 'name')
    
    def __str__(self):
        return f"{self.university.code} - {self.name}"
