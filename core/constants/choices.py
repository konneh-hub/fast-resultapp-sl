"""
Core constants used across the application
"""

class UserRole:
    """User role choices"""
    ADMIN = 'admin'
    REGISTRAR = 'registrar'
    DEPARTMENT_HEAD = 'department_head'
    LECTURER = 'lecturer'
    STUDENT = 'student'
    CLERK = 'clerk'
    
    CHOICES = [
        (ADMIN, 'Administrator'),
        (REGISTRAR, 'Registrar'),
        (DEPARTMENT_HEAD, 'Department Head'),
        (LECTURER, 'Lecturer'),
        (STUDENT, 'Student'),
        (CLERK, 'Clerk'),
    ]


class ResultStatus:
    """Result status choices"""
    PENDING = 'pending'
    SUBMITTED = 'submitted'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    PUBLISHED = 'published'
    
    CHOICES = [
        (PENDING, 'Pending'),
        (SUBMITTED, 'Submitted'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (PUBLISHED, 'Published'),
    ]


class ApprovalStatus:
    """Approval status choices"""
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    AWAITING_CORRECTION = 'awaiting_correction'
    
    CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (AWAITING_CORRECTION, 'Awaiting Correction'),
    ]


class StudentStatus:
    """Student enrollment status"""
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    SUSPENDED = 'suspended'
    GRADUATED = 'graduated'
    DEFERRED = 'deferred'
    WITHDRAWN = 'withdrawn'
    
    CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (SUSPENDED, 'Suspended'),
        (GRADUATED, 'Graduated'),
        (DEFERRED, 'Deferred'),
        (WITHDRAWN, 'Withdrawn'),
    ]


class GradeType:
    """Grade calculation type"""
    LETTER = 'letter'
    NUMERIC = 'numeric'
    PERCENTAGE = 'percentage'
    
    CHOICES = [
        (LETTER, 'Letter Grade'),
        (NUMERIC, 'Numeric Grade'),
        (PERCENTAGE, 'Percentage'),
    ]


class ExamType:
    """Exam type choices"""
    MIDTERM = 'midterm'
    FINAL = 'final'
    PRACTICAL = 'practical'
    PROJECT = 'project'
    ASSIGNMENT = 'assignment'
    
    CHOICES = [
        (MIDTERM, 'Mid-term'),
        (FINAL, 'Final'),
        (PRACTICAL, 'Practical'),
        (PROJECT, 'Project'),
        (ASSIGNMENT, 'Assignment'),
    ]


class Semester:
    """Semester choices"""
    FIRST = '1'
    SECOND = '2'
    SUMMER = 'summer'
    
    CHOICES = [
        (FIRST, 'First Semester'),
        (SECOND, 'Second Semester'),
        (SUMMER, 'Summer Semester'),
    ]
