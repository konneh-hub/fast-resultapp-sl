"""
Application constants used throughout the system.
"""

# User Roles
ROLE_CHOICES = (
    ('student', 'Student'),
    ('lecturer', 'Lecturer'),
    ('academic_officer', 'Academic Officer'),
    ('university_admin', 'University Admin'),
    ('system_admin', 'System Admin'),
)

# Result Statuses
RESULT_STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('submitted', 'Submitted'),
    ('pending_approval', 'Pending Approval'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('released', 'Released'),
)

# Grade Choices
GRADE_CHOICES = (
    ('A', 'A (4.0)'),
    ('A-', 'A- (3.7)'),
    ('B+', 'B+ (3.3)'),
    ('B', 'B (3.0)'),
    ('B-', 'B- (2.7)'),
    ('C+', 'C+ (2.3)'),
    ('C', 'C (2.0)'),
    ('C-', 'C- (1.7)'),
    ('D+', 'D+ (1.3)'),
    ('D', 'D (1.0)'),
    ('F', 'F (0.0)'),
)

# Approval Statuses
APPROVAL_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
)

# Exam Types
EXAM_TYPE_CHOICES = (
    ('midterm', 'Midterm'),
    ('final', 'Final'),
    ('practical', 'Practical'),
    ('assignment', 'Assignment'),
)

# Student Status
STUDENT_STATUS_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('graduated', 'Graduated'),
    ('expelled', 'Expelled'),
    ('suspended', 'Suspended'),
)

# Payment Status
PAYMENT_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
)

# Semester Types
SEMESTER_CHOICES = (
    ('spring', 'Spring'),
    ('summer', 'Summer'),
    ('fall', 'Fall'),
)

# Maximum file upload sizes
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
MAX_BULK_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB
