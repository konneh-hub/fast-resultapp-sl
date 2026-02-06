"""
Lecturers app serializers
"""
from rest_framework import serializers
from lecturers.models import LecturerProfile, LecturerQualification


class LecturerQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerQualification
        fields = ['id', 'lecturer', 'qualification_type', 'field_of_study', 'institution', 'year_obtained']


class LecturerProfileSerializer(serializers.ModelSerializer):
    user_full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    qualifications = LecturerQualificationSerializer(many=True, read_only=True)
    
    class Meta:
        model = LecturerProfile
        fields = ['id', 'user', 'user_full_name', 'staff_id', 'university', 'campus', 'department', 
                  'title', 'phone_number', 'office_location', 'is_active', 'qualifications', 'created_at']
        read_only_fields = ['created_at']
