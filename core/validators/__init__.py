"""
Shared validators for common validation patterns.
"""
import re
from django.core.exceptions import ValidationError


def validate_student_id(value):
    """Validate student ID format."""
    if not re.match(r'^[A-Z]{2}\d{6}$', value):
        raise ValidationError('Invalid student ID format. Expected format: XX123456')


def validate_email_domain(value):
    """Validate email domain."""
    if not value.endswith('.edu') and not value.endswith('.ac.uk'):
        raise ValidationError('Email must be from an educational institution.')


def validate_phone_number(value):
    """Validate phone number format."""
    if not re.match(r'^\+?[\d\s\-\(\)]{10,}$', value):
        raise ValidationError('Invalid phone number format.')


def validate_gpa(value):
    """Validate GPA is between 0 and 4.0."""
    if not 0 <= value <= 4.0:
        raise ValidationError('GPA must be between 0 and 4.0')


def validate_percentage(value):
    """Validate value is between 0 and 100."""
    if not 0 <= value <= 100:
        raise ValidationError('Value must be between 0 and 100')
