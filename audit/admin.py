"""
Django admin configuration for audit app
"""
from django.contrib import admin
from audit.models import ActivityLog, LoginLog, ResultChangeLog, ApprovalLog


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'content_type', 'created_at')
    list_filter = ('action', 'content_type', 'created_at')
    search_fields = ('user__username', 'content_type')
    readonly_fields = ('created_at',)


@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time', 'logout_time', 'ip_address', 'is_successful')
    list_filter = ('is_successful', 'login_time')
    search_fields = ('user__username', 'ip_address')


@admin.register(ResultChangeLog)
class ResultChangeLogAdmin(admin.ModelAdmin):
    list_display = ('result', 'changed_by', 'change_type', 'created_at')
    list_filter = ('change_type', 'created_at')


@admin.register(ApprovalLog)
class ApprovalLogAdmin(admin.ModelAdmin):
    list_display = ('approval_action', 'actor', 'action', 'created_at')
    list_filter = ('action', 'created_at')
