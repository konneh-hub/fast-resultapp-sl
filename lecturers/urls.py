"""
Lecturers app URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lecturers.views import LecturerProfileViewSet

router = DefaultRouter()
router.register(r'profiles', LecturerProfileViewSet, basename='lecturer-profile')

urlpatterns = [
    path('', include(router.urls)),
]
