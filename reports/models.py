"""
Reports app - Analytics and data exports
"""
from django.db import models
from core.mixins import TimestampMixin


class ReportTemplate(TimestampMixin):
    """Report template definitions"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    report_type = models.CharField(
        max_length=50,
        choices=[
            ('academic', 'Academic Report'),
            ('financial', 'Financial Report'),
            ('enrollment', 'Enrollment Report'),
            ('results', 'Results Report'),
        ]
    )
    query = models.JSONField()
    created_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class GeneratedReport(TimestampMixin):
    """Generated report instances"""
    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE)
    file = models.FileField(upload_to='reports/%Y/%m/%d/')
    generated_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    parameters = models.JSONField(default=dict)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.template.name} - {self.created_at.date()}"
