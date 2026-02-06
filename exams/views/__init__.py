"""
Exams app views
"""
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from exams.models import ExamPeriod, ExamCalendar, ExamRoom, InvigilatorAssignment
from core.pagination import StandardPagination


class ExamPeriodViewSet(viewsets.ModelViewSet):
    queryset = ExamPeriod.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['semester', 'exam_type', 'is_active']
    search_fields = ['name']


class ExamCalendarViewSet(viewsets.ModelViewSet):
    queryset = ExamCalendar.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam_period', 'course', 'exam_date']


class ExamRoomViewSet(viewsets.ModelViewSet):
    queryset = ExamRoom.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['campus', 'is_available']
    search_fields = ['room_code', 'location']


class InvigilatorAssignmentViewSet(viewsets.ModelViewSet):
    queryset = InvigilatorAssignment.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam_calendar', 'lecturer', 'room', 'status']
