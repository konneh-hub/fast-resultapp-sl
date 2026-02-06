"""
Students app views
"""
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from students.models import StudentProfile, StudentEnrollment, EnrolledCourse, StudentDocument
from students.serializers import (
    StudentProfileSerializer, StudentEnrollmentSerializer, 
    EnrolledCourseSerializer, StudentDocumentSerializer
)
from core.pagination import StandardPagination


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['university', 'program', 'status', 'is_international']
    search_fields = ['student_id', 'user__first_name', 'user__last_name']
    ordering_fields = ['student_id', 'created_at']
    
    @action(detail=True, methods=['get'])
    def enrollments(self, request, pk=None):
        """Get all enrollments for a student"""
        student = self.get_object()
        enrollments = student.enrollments.all()
        serializer = StudentEnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)


class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = StudentEnrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'program', 'academic_year', 'semester', 'is_registered']


class EnrolledCourseViewSet(viewsets.ModelViewSet):
    queryset = EnrolledCourse.objects.all()
    serializer_class = EnrolledCourseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['enrollment', 'course', 'is_retake']


class StudentDocumentViewSet(viewsets.ModelViewSet):
    queryset = StudentDocument.objects.all()
    serializer_class = StudentDocumentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'document_type']
