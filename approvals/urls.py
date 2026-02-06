"""
Approvals app URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from approvals.views import (
    SubmissionViewSet, ApprovalStageViewSet, 
    ApprovalActionViewSet, CorrectionRequestViewSet
)

router = DefaultRouter()
router.register(r'submissions', SubmissionViewSet, basename='submission')
router.register(r'approval-stages', ApprovalStageViewSet, basename='approval-stage')
router.register(r'approval-actions', ApprovalActionViewSet, basename='approval-action')
router.register(r'correction-requests', CorrectionRequestViewSet, basename='correction-request')

urlpatterns = [
    path('', include(router.urls)),
]
