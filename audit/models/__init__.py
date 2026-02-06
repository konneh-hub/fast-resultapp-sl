"""
Audit app models - Track system activities
"""
from django.db import models
from django.contrib.auth.models import User
from core.mixins import TimestampMixin


class ActivityLog(TimestampMixin):
    """General activity log"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='activity_logs')
    action = models.CharField(
        max_length=20,
        choices=[
            ('create', 'Create'),
            ('update', 'Update'),
            ('delete', 'Delete'),
            ('view', 'View'),
            ('download', 'Download'),
            ('export', 'Export'),
        ]
    )
    content_type = models.CharField(max_length=100)
    object_id = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    changes = models.JSONField(default=dict, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['content_type', 'object_id']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.action} on {self.content_type}"


class LoginLog(TimestampMixin):
    """User login/logout logs"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='login_logs')
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    is_successful = models.BooleanField(default=True)
    failure_reason = models.CharField(max_length=255, blank=True)
    
    class Meta:
        ordering = ['-login_time']
        indexes = [
            models.Index(fields=['user', '-login_time']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.login_time}"


class ResultChangeLog(TimestampMixin):
    """Track result modifications"""
    from results.models import Result
    
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='change_logs')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    change_type = models.CharField(
        max_length=20,
        choices=[
            ('score_update', 'Score Update'),
            ('grade_update', 'Grade Update'),
            ('status_change', 'Status Change'),
        ]
    )
    old_value = models.JSONField()
    new_value = models.JSONField()
    reason = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.result.course.code} - {self.change_type}"


class ApprovalLog(TimestampMixin):
    """Track approval workflow changes"""
    from approvals.models import ApprovalAction
    
    approval_action = models.ForeignKey(ApprovalAction, on_delete=models.CASCADE, related_name='logs')
    actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(
        max_length=50,
        choices=[
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('correction_requested', 'Correction Requested'),
            ('reassigned', 'Reassigned'),
        ]
    )
    comments = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Approval Log - {self.approval_action.submission.enrollment.student.student_id}"
