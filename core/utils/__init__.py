"""
Shared utility functions for common operations.
"""
import uuid
from datetime import datetime, timedelta


def generate_uuid():
    """Generate a unique UUID."""
    return uuid.uuid4()


def get_current_semester():
    """Get current semester based on month."""
    month = datetime.now().month
    year = datetime.now().year
    
    if month in [1, 2, 3, 4, 5]:
        return f'Spring {year}'
    elif month in [6, 7, 8]:
        return f'Summer {year}'
    else:
        return f'Fall {year}'


def get_academic_year():
    """Get current academic year."""
    today = datetime.now()
    if today.month >= 9:
        return f'{today.year}-{today.year + 1}'
    else:
        return f'{today.year - 1}-{today.year}'


def format_gpa(gpa_value):
    """Format GPA to 2 decimal places."""
    return round(float(gpa_value), 2)


def calculate_days_until_date(target_date):
    """Calculate days until a specific date."""
    return (target_date - datetime.now()).days
