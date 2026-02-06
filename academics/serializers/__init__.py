"""
Academics app serializers
"""
from rest_framework import serializers
from academics.models import Faculty, Department, Program, Course, CourseAllocation


class FacultySerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name', read_only=True)
    
    class Meta:
        model = Faculty
        fields = ['id', 'university', 'university_name', 'name', 'code', 'description', 'is_active', 'created_at']
        read_only_fields = ['created_at']


class DepartmentSerializer(serializers.ModelSerializer):
    faculty_name = serializers.CharField(source='faculty.name', read_only=True)
    university_code = serializers.CharField(source='faculty.university.code', read_only=True)
    
    class Meta:
        model = Department
        fields = ['id', 'faculty', 'faculty_name', 'university_code', 'name', 'code', 'description', 'is_active', 'created_at']
        read_only_fields = ['created_at']


class ProgramSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)
    
    class Meta:
        model = Program
        fields = ['id', 'department', 'department_name', 'name', 'code', 'level', 'duration_years', 'total_credits', 'description', 'is_active', 'created_at']
        read_only_fields = ['created_at']


class CourseSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.name', read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'program', 'program_name', 'name', 'code', 'description', 'credit_units', 'level', 'is_compulsory', 'is_active', 'created_at']
        read_only_fields = ['created_at']


class CourseAllocationSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    lecturer_name = serializers.CharField(source='lecturer.user.get_full_name', read_only=True)
    
    class Meta:
        model = CourseAllocation
        fields = ['id', 'course', 'course_name', 'lecturer', 'lecturer_name', 'semester', 'is_coordinator', 'created_at']
        read_only_fields = ['created_at']
