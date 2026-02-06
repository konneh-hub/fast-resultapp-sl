"""
Audit helper functions for tracking changes and activity.
"""
import json
from datetime import datetime


class AuditLogger:
    """Helper class for logging audit trails."""
    
    @staticmethod
    def log_change(model_name, object_id, action, changes, user=None):
        """Log a change to the audit log."""
        from audit.models import ActivityLog
        
        ActivityLog.objects.create(
            model_name=model_name,
            object_id=object_id,
            action=action,
            changes=json.dumps(changes),
            user=user,
            timestamp=datetime.now()
        )
    
    @staticmethod
    def log_login(user, ip_address):
        """Log user login."""
        from audit.models import LoginLog
        
        LoginLog.objects.create(
            user=user,
            ip_address=ip_address,
            timestamp=datetime.now()
        )
    
    @staticmethod
    def log_result_change(result_id, changes, user=None):
        """Log result changes."""
        AuditLogger.log_change('Result', result_id, 'UPDATE', changes, user)
