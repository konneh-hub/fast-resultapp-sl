"""
Shared permissions for access control across the application.
"""
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Only admin users can access."""
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsUniversityAdmin(BasePermission):
    """Only university admins can access."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'profile') and request.user.profile.role == 'university_admin'


class IsAcademicOfficer(BasePermission):
    """Only academic officers can access."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'profile') and request.user.profile.role == 'academic_officer'


class IsLecturer(BasePermission):
    """Only lecturers can access."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'profile') and request.user.profile.role == 'lecturer'


class IsStudent(BasePermission):
    """Only students can access."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'profile') and request.user.profile.role == 'student'
