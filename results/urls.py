"""
Results app URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from results.views import (
    ResultViewSet, GPARecordViewSet, CGPARecordViewSet, 
    TranscriptViewSet, ResultLockViewSet, ResultReleaseViewSet
)

router = DefaultRouter()
router.register(r'results', ResultViewSet, basename='result')
router.register(r'gpa-records', GPARecordViewSet, basename='gpa-record')
router.register(r'cgpa-records', CGPARecordViewSet, basename='cgpa-record')
router.register(r'transcripts', TranscriptViewSet, basename='transcript')
router.register(r'result-locks', ResultLockViewSet, basename='result-lock')
router.register(r'result-releases', ResultReleaseViewSet, basename='result-release')

urlpatterns = [
    path('', include(router.urls)),
]
