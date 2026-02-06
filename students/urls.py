"""
Students app URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import (
    StudentProfileViewSet, StudentEnrollmentViewSet, 
    EnrolledCourseViewSet, StudentDocumentViewSet
)

router = DefaultRouter()
router.register(r'profiles', StudentProfileViewSet, basename='student-profile')
router.register(r'enrollments', StudentEnrollmentViewSet, basename='enrollment')
router.register(r'enrolled-courses', EnrolledCourseViewSet, basename='enrolled-course')
router.register(r'documents', StudentDocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
]
