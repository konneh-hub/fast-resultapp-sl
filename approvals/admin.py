"""
Django admin configuration for approvals app
"""
from django.contrib import admin
from approvals.models import Submission, ApprovalStage, ApprovalAction, ApprovalHistory, CorrectionRequest


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'submission_type', 'submission_date', 'submitted_by')
    list_filter = ('submission_type', 'submission_date')


@admin.register(ApprovalStage)
class ApprovalStageAdmin(admin.ModelAdmin):
    list_display = ('stage_number', 'stage_name', 'university', 'required_role', 'is_active')
    list_filter = ('required_role', 'is_active')


@admin.register(ApprovalAction)
class ApprovalActionAdmin(admin.ModelAdmin):
    list_display = ('submission', 'approval_stage', 'status', 'assigned_to', 'action_date')
    list_filter = ('status', 'approval_stage')


@admin.register(ApprovalHistory)
class ApprovalHistoryAdmin(admin.ModelAdmin):
    list_display = ('approval_action', 'previous_status', 'new_status', 'changed_by')
    list_filter = ('new_status', 'created_at')


@admin.register(CorrectionRequest)
class CorrectionRequestAdmin(admin.ModelAdmin):
    list_display = ('approval_action', 'status', 'requested_by', 'created_at')
    list_filter = ('status', 'created_at')
