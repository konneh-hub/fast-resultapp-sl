"""
Exams app models
"""
from django.db import models
from core.mixins import TimestampMixin, AuditMixin
from universities.models import Semester, Campus
from academics.models import Course
from lecturers.models import LecturerProfile


class ExamPeriod(AuditMixin):
    """Exam period within a semester"""
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='exam_periods')
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    exam_type = models.CharField(
        max_length=20,
        choices=[
            ('midterm', 'Mid-term'),
            ('final', 'Final'),
            ('supplementary', 'Supplementary'),
        ]
    )
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('semester', 'exam_type')
        ordering = ['start_date']
    
    def __str__(self):
        return f"{self.semester.name} - {self.name}"


class ExamCalendar(AuditMixin):
    """Individual exam schedule"""
    exam_period = models.ForeignKey(ExamPeriod, on_delete=models.CASCADE, related_name='calendars')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration_minutes = models.IntegerField()
    venue = models.CharField(max_length=255)
    invigilators_count = models.IntegerField(default=2)
    
    class Meta:
        unique_together = ('exam_period', 'course')
        ordering = ['exam_date', 'start_time']
    
    def __str__(self):
        return f"{self.course.code} - {self.exam_date}"


class ExamRoom(TimestampMixin):
    """Exam room/venue"""
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='exam_rooms')
    room_code = models.CharField(max_length=20)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('campus', 'room_code')
    
    def __str__(self):
        return f"{self.campus.name} - {self.room_code} (Cap: {self.capacity})"


class InvigilatorAssignment(AuditMixin):
    """Assignment of invigilators to exams"""
    exam_calendar = models.ForeignKey(ExamCalendar, on_delete=models.CASCADE, related_name='invigilators')
    lecturer = models.ForeignKey(LecturerProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(ExamRoom, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('assigned', 'Assigned'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('absent', 'Absent'),
        ],
        default='assigned'
    )
    
    class Meta:
        unique_together = ('exam_calendar', 'lecturer', 'room')
    
    def __str__(self):
        return f"{self.exam_calendar.course.code} - {self.lecturer.user.last_name}"
