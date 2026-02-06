"""
Universities app URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from universities.views import (
    UniversityViewSet, CampusViewSet, AcademicYearViewSet, 
    SemesterViewSet, GradingScaleViewSet, CreditRulesViewSet
)

router = DefaultRouter()
router.register(r'universities', UniversityViewSet, basename='university')
router.register(r'campuses', CampusViewSet, basename='campus')
router.register(r'academic-years', AcademicYearViewSet, basename='academic-year')
router.register(r'semesters', SemesterViewSet, basename='semester')
router.register(r'grading-scales', GradingScaleViewSet, basename='grading-scale')
router.register(r'credit-rules', CreditRulesViewSet, basename='credit-rules')

urlpatterns = [
    path('', include(router.urls)),
]
