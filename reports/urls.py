"""
Reports app URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import ReportTemplateViewSet, GeneratedReportViewSet

router = DefaultRouter()
router.register(r'templates', ReportTemplateViewSet, basename='report-template')
router.register(r'generated', GeneratedReportViewSet, basename='generated-report')

urlpatterns = [
    path('', include(router.urls)),
]
