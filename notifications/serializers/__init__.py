"""
Notifications app serializers
"""
from rest_framework import serializers
from notifications.models import Notification, Announcement, Broadcast


class NotificationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'user', 'user_name', 'title', 'message', 'notification_type', 'is_read', 
                  'read_at', 'related_object_id', 'created_at']
        read_only_fields = ['created_at']


class AnnouncementSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user.get_full_name', read_only=True)
    
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'content', 'created_by', 'created_by_name', 'is_active', 
                  'published_date', 'expiry_date', 'created_at']
        read_only_fields = ['created_at']


class BroadcastSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user.get_full_name', read_only=True)
    
    class Meta:
        model = Broadcast
        fields = ['id', 'title', 'message', 'recipient_group', 'created_by', 'created_by_name', 
                  'sent_date', 'created_at']
        read_only_fields = ['created_at']
