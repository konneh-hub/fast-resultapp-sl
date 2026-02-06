"""
Approvals app serializers
"""
from rest_framework import serializers
from approvals.models import Submission, ApprovalStage, ApprovalAction, ApprovalHistory, CorrectionRequest


class ApprovalStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalStage
        fields = ['id', 'university', 'stage_number', 'stage_name', 'description', 'required_role', 
                  'can_reject', 'can_request_correction', 'is_active']


class CorrectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectionRequest
        fields = ['id', 'approval_action', 'requested_by', 'reason', 'details', 'status', 'completed_date', 'created_at']
        read_only_fields = ['created_at']


class ApprovalHistorySerializer(serializers.ModelSerializer):
    changed_by_name = serializers.CharField(source='changed_by.user.get_full_name', read_only=True)
    
    class Meta:
        model = ApprovalHistory
        fields = ['id', 'approval_action', 'previous_status', 'new_status', 'changed_by', 'changed_by_name', 
                  'change_reason', 'created_at']
        read_only_fields = ['created_at']


class ApprovalActionSerializer(serializers.ModelSerializer):
    correction_requests = CorrectionRequestSerializer(many=True, read_only=True)
    history = ApprovalHistorySerializer(many=True, read_only=True)
    stage_name = serializers.CharField(source='approval_stage.stage_name', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to.user.get_full_name', read_only=True)
    
    class Meta:
        model = ApprovalAction
        fields = ['id', 'submission', 'approval_stage', 'stage_name', 'assigned_to', 'assigned_to_name', 'status', 
                  'action_date', 'comments', 'correction_requests', 'history', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class SubmissionSerializer(serializers.ModelSerializer):
    approvals = ApprovalActionSerializer(many=True, read_only=True)
    student_id = serializers.CharField(source='enrollment.student.student_id', read_only=True)
    submitted_by_name = serializers.CharField(source='submitted_by.user.get_full_name', read_only=True)
    
    class Meta:
        model = Submission
        fields = ['id', 'enrollment', 'student_id', 'submission_type', 'submitted_by', 'submitted_by_name', 
                  'submission_date', 'notes', 'approvals', 'created_at']
        read_only_fields = ['submission_date', 'created_at']
