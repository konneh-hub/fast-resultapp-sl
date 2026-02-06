"""
Exams app URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from exams.views import (
    ExamPeriodViewSet, ExamCalendarViewSet, ExamRoomViewSet, InvigilatorAssignmentViewSet
)

router = DefaultRouter()
router.register(r'exam-periods', ExamPeriodViewSet, basename='exam-period')
router.register(r'exam-calendars', ExamCalendarViewSet, basename='exam-calendar')
router.register(r'exam-rooms', ExamRoomViewSet, basename='exam-room')
router.register(r'invigilator-assignments', InvigilatorAssignmentViewSet, basename='invigilator-assignment')

urlpatterns = [
    path('', include(router.urls)),
]
