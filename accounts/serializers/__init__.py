"""
Accounts app serializers
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import UserProfile, PasswordReset


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']
        read_only_fields = ['id']


class UserProfileSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    university_name = serializers.CharField(source='university.name', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'user_details', 'university', 'university_name', 'role', 'phone_number', 'avatar', 'is_verified', 'created_at']
        read_only_fields = ['created_at']


class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordReset
        fields = ['id', 'user', 'token', 'is_used', 'expires_at', 'created_at']
        read_only_fields = ['token', 'created_at']
