# dashboard/admin.py

from django.contrib import admin
from dashboard.models import DashboardUserPreference, DashboardActivity

# Only register dashboard-specific models
@admin.register(DashboardUserPreference)
class DashboardUserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'items_per_page', 'default_view', 'color_theme', 'email_notifications')
    list_filter = ('default_view', 'color_theme', 'email_notifications')
    search_fields = ('user__username', 'user__email')


@admin.register(DashboardActivity)
class DashboardActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'content_type', 'object_str', 'timestamp', 'ip_address')
    list_filter = ('action', 'content_type', 'timestamp')
    search_fields = ('user__username', 'action', 'object_str')
    readonly_fields = ('user', 'action', 'content_type', 'object_id', 'object_str', 'timestamp', 'ip_address')
    
    def has_add_permission(self, request):
        return False  # Prevent adding activity logs manually
        
    def has_change_permission(self, request, obj=None):
        return False  # Prevent changing activity logs