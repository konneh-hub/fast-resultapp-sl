"""
Approvals app views
"""
from django.utils import timezone
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from approvals.models import Submission, ApprovalStage, ApprovalAction, CorrectionRequest
from approvals.serializers import (
    SubmissionSerializer, ApprovalStageSerializer, 
    ApprovalActionSerializer, CorrectionRequestSerializer
)
from core.pagination import StandardPagination


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['enrollment', 'submission_type']
    search_fields = ['enrollment__student__student_id']


class ApprovalStageViewSet(viewsets.ModelViewSet):
    queryset = ApprovalStage.objects.all()
    serializer_class = ApprovalStageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['university', 'required_role', 'is_active']


class ApprovalActionViewSet(viewsets.ModelViewSet):
    queryset = ApprovalAction.objects.all()
    serializer_class = ApprovalActionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['submission', 'approval_stage', 'assigned_to', 'status']
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Approve a submission"""
        approval = self.get_object()
        approval.status = 'approved'
        approval.action_date = timezone.now()
        approval.save()
        serializer = self.get_serializer(approval)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """Reject a submission"""
        approval = self.get_object()
        approval.status = 'rejected'
        approval.action_date = timezone.now()
        approval.comments = request.data.get('reason', '')
        approval.save()
        serializer = self.get_serializer(approval)
        return Response(serializer.data)


class CorrectionRequestViewSet(viewsets.ModelViewSet):
    queryset = CorrectionRequest.objects.all()
    serializer_class = CorrectionRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['approval_action', 'status']
