"""
Approvals app models - Multi-level approval workflow
"""
from django.db import models
from core.mixins import TimestampMixin, AuditMixin
from core.constants import APPROVAL_STATUS_CHOICES
from students.models import StudentEnrollment


class Submission(AuditMixin):
    """Result submission for approval"""
    enrollment = models.ForeignKey(StudentEnrollment, on_delete=models.CASCADE, related_name='submissions')
    submission_type = models.CharField(
        max_length=20,
        choices=[
            ('initial', 'Initial Submission'),
            ('resubmission', 'Resubmission'),
            ('correction', 'Correction'),
        ]
    )
    submitted_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-submission_date']
    
    def __str__(self):
        return f"{self.enrollment.student.student_id} - {self.submission_type}"


class ApprovalStage(AuditMixin):
    """Defines approval workflow stages"""
    from universities.models import University
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='approval_stages')
    stage_number = models.IntegerField()
    stage_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    required_role = models.CharField(
        max_length=50,
        choices=[
            ('department_head', 'Department Head'),
            ('college_registrar', 'College Registrar'),
            ('university_registrar', 'University Registrar'),
            ('admin', 'Administrator'),
        ]
    )
    can_reject = models.BooleanField(default=True)
    can_request_correction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('university', 'stage_number')
        ordering = ['stage_number']
    
    def __str__(self):
        return f"{self.stage_name} (Stage {self.stage_number})"


class ApprovalAction(AuditMixin):
    """Individual approval action on a submission"""
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='approvals')
    approval_stage = models.ForeignKey(ApprovalStage, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=20,
        choices=APPROVAL_STATUS_CHOICES,
        default='pending'
    )
    action_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('submission', 'approval_stage')
        ordering = ['approval_stage', '-created_at']
    
    def __str__(self):
        return f"{self.submission.enrollment.student.student_id} - {self.approval_stage.stage_name} ({self.status})"


class ApprovalHistory(TimestampMixin):
    """Historical record of all approval changes"""
    approval_action = models.ForeignKey(ApprovalAction, on_delete=models.CASCADE, related_name='history')
    previous_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    change_reason = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Approval Histories'
    
    def __str__(self):
        return f"{self.approval_action.submission.enrollment.student.student_id} - {self.new_status}"


class CorrectionRequest(AuditMixin):
    """Request for result correction during approval"""
    approval_action = models.ForeignKey(ApprovalAction, on_delete=models.CASCADE, related_name='correction_requests')
    requested_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    reason = models.TextField()
    details = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('rejected', 'Rejected'),
        ],
        default='pending'
    )
    completed_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Correction Request - {self.approval_action.submission.enrollment.student.student_id}"
