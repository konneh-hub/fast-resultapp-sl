"""
Universities app serializers
"""
from rest_framework import serializers
from universities.models import (
    University, Campus, AcademicYear, Semester, GradingScale, GradePoint, CreditRules
)


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'code', 'abbreviation', 'description', 'website', 'country', 'city', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CampusSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name', read_only=True)
    
    class Meta:
        model = Campus
        fields = ['id', 'university', 'university_name', 'name', 'code', 'location', 'is_main', 'is_active', 'created_at']
        read_only_fields = ['created_at']


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = ['id', 'university', 'year', 'start_date', 'end_date', 'is_current', 'is_active', 'created_at']
        read_only_fields = ['created_at']


class SemesterSerializer(serializers.ModelSerializer):
    academic_year_display = serializers.CharField(source='academic_year.year', read_only=True)
    
    class Meta:
        model = Semester
        fields = ['id', 'academic_year', 'academic_year_display', 'name', 'number', 'start_date', 'end_date', 
                  'registration_start', 'registration_end', 'exam_start', 'exam_end', 'is_current', 'is_active', 'created_at']
        read_only_fields = ['created_at']


class GradePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradePoint
        fields = ['id', 'grading_scale', 'grade', 'min_score', 'max_score', 'point_value']


class GradingScaleSerializer(serializers.ModelSerializer):
    grade_points = GradePointSerializer(many=True, read_only=True)
    
    class Meta:
        model = GradingScale
        fields = ['id', 'university', 'name', 'description', 'scale_type', 'min_score', 'max_score', 'is_active', 'grade_points', 'created_at']
        read_only_fields = ['created_at']


class CreditRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditRules
        fields = ['id', 'university', 'name', 'minimum_credits_per_semester', 'maximum_credits_per_semester', 
                  'minimum_gpa_for_graduation', 'minimum_gpa_for_good_standing', 'pass_grade', 'created_at']
        read_only_fields = ['created_at']
