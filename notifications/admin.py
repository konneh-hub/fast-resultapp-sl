"""
Django admin configuration for notifications app
"""
from django.contrib import admin
from notifications.models import Notification, Announcement, Broadcast


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('user__username', 'title')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'expiry_date', 'is_active')
    list_filter = ('is_active', 'published_date')
    search_fields = ('title', 'content')


@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipient_group', 'sent_date', 'created_by')
    list_filter = ('recipient_group', 'sent_date')
    search_fields = ('title',)
