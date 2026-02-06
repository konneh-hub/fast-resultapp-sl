"""
Lecturers app models
"""
from django.db import models
from django.contrib.auth.models import User
from core.mixins import TimestampMixin, AuditMixin
from universities.models import University, Campus
from academics.models import Department


class LecturerProfile(AuditMixin):
    """Extended lecturer profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer_profile')
    staff_id = models.CharField(max_length=20, unique=True)
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='lecturers')
    title = models.CharField(
        max_length=50,
        choices=[
            ('professor', 'Professor'),
            ('associate', 'Associate Professor'),
            ('senior', 'Senior Lecturer'),
            ('lecturer', 'Lecturer'),
            ('assistant', 'Assistant Lecturer'),
        ]
    )
    phone_number = models.CharField(max_length=20)
    office_location = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['staff_id']
    
    def __str__(self):
        return f"{self.staff_id} - {self.user.get_full_name()}"


class LecturerQualification(TimestampMixin):
    """Lecturer qualifications/credentials"""
    lecturer = models.ForeignKey(LecturerProfile, on_delete=models.CASCADE, related_name='qualifications')
    qualification_type = models.CharField(
        max_length=20,
        choices=[
            ('diploma', 'Diploma'),
            ('bachelors', "Bachelor's"),
            ('masters', "Master's"),
            ('phd', 'PhD'),
        ]
    )
    field_of_study = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year_obtained = models.IntegerField()
    
    class Meta:
        ordering = ['-year_obtained']
    
    def __str__(self):
        return f"{self.lecturer.user.last_name} - {self.qualification_type} in {self.field_of_study}"
