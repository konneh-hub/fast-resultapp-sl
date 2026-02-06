"""
Accounts app models - User authentication and profiles
"""
from django.db import models
from django.contrib.auth.models import User
from core.mixins import TimestampMixin, AuditMixin
from core.constants import ROLE_CHOICES
from universities.models import University


class UserProfile(AuditMixin):
    """Extended user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )
    phone_number = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['user__last_name']
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.role})"


class PasswordReset(TimestampMixin):
    """Password reset tokens"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_resets')
    token = models.CharField(max_length=255, unique=True)
    is_used = models.BooleanField(default=False)
    expires_at = models.DateTimeField()
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Reset for {self.user.username}"
