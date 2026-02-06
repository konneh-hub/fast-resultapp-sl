"""
Django admin configuration for accounts app
"""
from django.contrib import admin
from accounts.models import UserProfile, PasswordReset


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'university', 'role', 'is_verified', 'created_at')
    list_filter = ('role', 'is_verified', 'university')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(PasswordReset)
class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_used', 'expires_at', 'created_at')
    list_filter = ('is_used', 'expires_at')
