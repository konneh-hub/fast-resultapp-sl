"""
Notifications app models
"""
from django.db import models
from django.contrib.auth.models import User
from core.mixins import TimestampMixin


class Notification(TimestampMixin):
    """Individual user notifications"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    notification_type = models.CharField(
        max_length=50,
        choices=[
            ('result_published', 'Result Published'),
            ('approval_needed', 'Approval Needed'),
            ('course_registered', 'Course Registered'),
            ('exam_scheduled', 'Exam Scheduled'),
            ('system', 'System'),
        ]
    )
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    related_object_id = models.CharField(max_length=255, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"


class Announcement(TimestampMixin):
    """System announcements"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    published_date = models.DateTimeField()
    expiry_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title


class Broadcast(TimestampMixin):
    """Broadcast messages to groups"""
    title = models.CharField(max_length=255)
    message = models.TextField()
    recipient_group = models.CharField(
        max_length=50,
        choices=[
            ('all', 'All Users'),
            ('students', 'Students'),
            ('lecturers', 'Lecturers'),
            ('admin', 'Admin'),
        ]
    )
    created_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    sent_date = models.DateTimeField()
    
    class Meta:
        ordering = ['-sent_date']
    
    def __str__(self):
        return self.title
