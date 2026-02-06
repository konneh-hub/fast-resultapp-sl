"""
Lecturers app views
"""
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from lecturers.models import LecturerProfile
from lecturers.serializers import LecturerProfileSerializer
from core.pagination import StandardPagination


class LecturerProfileViewSet(viewsets.ModelViewSet):
    queryset = LecturerProfile.objects.all()
    serializer_class = LecturerProfileSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['university', 'department', 'title', 'is_active']
    search_fields = ['staff_id', 'user__first_name', 'user__last_name']
    ordering_fields = ['staff_id', 'user__last_name']
