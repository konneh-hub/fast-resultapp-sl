"""
Results app views
"""
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from results.models import Result, GPARecord, CGPARecord, Transcript, ResultLock, ResultRelease
from results.serializers import (
    ResultSerializer, GPARecordSerializer, CGPARecordSerializer, 
    TranscriptSerializer, ResultLockSerializer, ResultReleaseSerializer
)
from core.pagination import StandardPagination


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['enrollment', 'course', 'status']
    search_fields = ['enrollment__student__student_id', 'course__code']


class GPARecordViewSet(viewsets.ModelViewSet):
    queryset = GPARecord.objects.all()
    serializer_class = GPARecordSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['enrollment', 'enrollment__student']


class CGPARecordViewSet(viewsets.ModelViewSet):
    queryset = CGPARecord.objects.all()
    serializer_class = CGPARecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['student']
    search_fields = ['student__student_id']


class TranscriptViewSet(viewsets.ModelViewSet):
    queryset = Transcript.objects.all()
    serializer_class = TranscriptSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'academic_year', 'is_official']


class ResultLockViewSet(viewsets.ModelViewSet):
    queryset = ResultLock.objects.all()
    serializer_class = ResultLockSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['enrollment', 'is_locked']


class ResultReleaseViewSet(viewsets.ModelViewSet):
    queryset = ResultRelease.objects.all()
    serializer_class = ResultReleaseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['semester', 'can_view_results']
