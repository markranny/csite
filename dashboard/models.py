# dashboard/models.py

from django.db import models


class DashboardUserPreference(models.Model):
    """Model to store dashboard user preferences"""
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='dashboard_preferences')
    
    # Display preferences
    items_per_page = models.PositiveIntegerField(default=10)
    default_view = models.CharField(
        max_length=20,
        choices=[
            ('list', 'List View'),
            ('grid', 'Grid View'),
        ],
        default='list'
    )
    
    # Theme preferences
    color_theme = models.CharField(
        max_length=20,
        choices=[
            ('light', 'Light Theme'),
            ('dark', 'Dark Theme'),
        ],
        default='light'
    )
    
    # Notification preferences
    email_notifications = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Dashboard Preference'
        verbose_name_plural = 'Dashboard Preferences'
    
    def __str__(self):
        return f"{self.user.username}'s Dashboard Preferences"


class DashboardActivity(models.Model):
    """Model to log dashboard activities for auditing"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='dashboard_activities')
    action = models.CharField(max_length=255)
    content_type = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object_str = models.CharField(max_length=255)  # String representation of the modified object
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Activity Log'
        verbose_name_plural = 'Activity Logs'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} {self.action} {self.object_str} at {self.timestamp}"
        choices=[
            ('light', 'Light Theme'),
            ('dark', 'Dark Theme'),
        ],
        default='light'
    )
    
    # Notification preferences
    email_notifications = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Dashboard Preference'
        verbose_name_plural = 'Dashboard Preferences'
    
    def __str__(self):
        return f"{self.user.username}'s Dashboard Preferences"
        choices=[
            ('light', 'Light Theme'),
            ('dark', 'Dark Theme'),
        ],
        default='light'
    )
    
    # Notification preferences
    email_notifications = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Dashboard Preference'
        verbose_name_plural = 'Dashboard Preferences'
    
    def __str__(self):
        return f"{self.user.username}'s Dashboard Preferences"


class DashboardActivity(models.Model):
    """Model to log dashboard activities for auditing"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='dashboard_activities')
    action = models.CharField(max_length=255)
    content_type = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object_str = models.CharField(max_length=255)  # String representation of the modified object
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Activity Log'
        verbose_name_plural = 'Activity Logs'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} {self.action} {self.object_str} at {self.timestamp}"