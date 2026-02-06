"""
Results app serializers
"""
from rest_framework import serializers
from results.models import (
    Result, ResultComponent, Grade, GPARecord, CGPARecord, Transcript, ResultLock, ResultRelease
)


class ResultComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultComponent
        fields = ['id', 'result', 'component_type', 'max_score', 'score_obtained', 'weight']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'result', 'total_score', 'letter_grade', 'grade_point', 'is_pass']


class ResultSerializer(serializers.ModelSerializer):
    components = ResultComponentSerializer(many=True, read_only=True)
    grade = GradeSerializer(read_only=True)
    course_code = serializers.CharField(source='course.code', read_only=True)
    student_id = serializers.CharField(source='enrollment.student.student_id', read_only=True)
    
    class Meta:
        model = Result
        fields = ['id', 'enrollment', 'course', 'course_code', 'student_id', 'status', 'submitted_by', 'submission_date', 
                  'components', 'grade', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class GPARecordSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source='enrollment.student.student_id', read_only=True)
    semester_info = serializers.SerializerMethodField()
    
    def get_semester_info(self, obj):
        return f"{obj.enrollment.academic_year.year} - {obj.enrollment.semester.name}"
    
    class Meta:
        model = GPARecord
        fields = ['id', 'enrollment', 'student_id', 'semester_info', 'semester_gpa', 'courses_taken', 'courses_passed', 
                  'total_points', 'total_credits', 'created_at']
        read_only_fields = ['created_at']


class CGPARecordSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    
    class Meta:
        model = CGPARecord
        fields = ['id', 'student', 'student_name', 'cumulative_gpa', 'total_courses_taken', 'total_courses_passed', 
                  'total_credits_earned', 'last_updated']
        read_only_fields = ['last_updated']


class TranscriptSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source='student.student_id', read_only=True)
    
    class Meta:
        model = Transcript
        fields = ['id', 'student', 'student_id', 'academic_year', 'is_official', 'generated_by', 'file', 'created_at']
        read_only_fields = ['created_at']


class ResultLockSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source='enrollment.student.student_id', read_only=True)
    
    class Meta:
        model = ResultLock
        fields = ['id', 'enrollment', 'student_id', 'is_locked', 'locked_by', 'locked_at', 'unlock_reason', 'created_at']
        read_only_fields = ['locked_at', 'created_at']


class ResultReleaseSerializer(serializers.ModelSerializer):
    semester_info = serializers.CharField(source='semester.name', read_only=True)
    
    class Meta:
        model = ResultRelease
        fields = ['id', 'semester', 'semester_info', 'can_view_results', 'released_date', 'released_by', 'created_at']
        read_only_fields = ['created_at']
