"""
Files app models
"""
from django.db import models
from core.mixins import TimestampMixin


class FileUpload(TimestampMixin):
    """Generic file upload tracking"""
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    file_type = models.CharField(max_length=50)
    file_size = models.BigIntegerField()
    uploaded_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.file.name}"


class TranscriptFile(TimestampMixin):
    """Transcript files"""
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE, related_name='transcript_files')
    file = models.FileField(upload_to='transcripts/%Y/%m/%d/')
    file_format = models.CharField(max_length=20, choices=[('pdf', 'PDF'), ('doc', 'DOC')])
    is_official = models.BooleanField(default=False)
    generated_by = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Transcript - {self.student.student_id}"
