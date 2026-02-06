"""
Students app serializers
"""
from rest_framework import serializers
from students.models import StudentProfile, StudentEnrollment, EnrolledCourse, StudentDocument


class StudentProfileSerializer(serializers.ModelSerializer):
    user_full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    program_name = serializers.CharField(source='program.name', read_only=True)
    university_name = serializers.CharField(source='university.name', read_only=True)
    
    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'user_full_name', 'student_id', 'university', 'university_name', 'campus', 'program', 'program_name', 
                  'date_of_birth', 'gender', 'phone_number', 'status', 'is_international', 'created_at']
        read_only_fields = ['created_at']


class EnrolledCourseSerializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source='course.code', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)
    
    class Meta:
        model = EnrolledCourse
        fields = ['id', 'enrollment', 'course', 'course_code', 'course_name', 'enrollment_date', 'is_retake', 'previous_grade']
        read_only_fields = ['enrollment_date']


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    courses = EnrolledCourseSerializer(many=True, read_only=True)
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    
    class Meta:
        model = StudentEnrollment
        fields = ['id', 'student', 'student_name', 'program', 'academic_year', 'semester', 'enrollment_date', 
                  'total_credits', 'is_registered', 'courses', 'created_at']
        read_only_fields = ['enrollment_date', 'created_at']


class StudentDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDocument
        fields = ['id', 'student', 'document_type', 'file', 'uploaded_by', 'created_at']
        read_only_fields = ['created_at']
