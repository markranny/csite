# dashboard/utils.py

from functools import wraps
from django.contrib import messages
from dashboard.models import DashboardUserPreference, DashboardActivity


def log_activity(action=None, content_type=None):
    """
    Decorator to log dashboard activities with more precision than middleware.
    
    Usage:
        @log_activity(action="updated", content_type="Site Settings")
        def site_settings(request):
            # View logic
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # First get the response
            response = view_func(request, *args, **kwargs)
            
            # Only log for POST requests with successful responses
            if request.method == 'POST' and response.status_code in [200, 301, 302]:
                # Determine object details
                object_id = kwargs.get('id') or kwargs.get('banner_id') or kwargs.get('section_id') or None
                
                # Determine object string representation
                object_str = None
                if hasattr(request, 'POST'):
                    for field in ['title', 'name', 'question', 'subject', 'label']:
                        if field in request.POST:
                            object_str = request.POST.get(field)[:255]
                            break
                
                if not object_str:
                    object_str = f"{content_type or 'Item'} {action or 'modified'}"
                
                # Get client IP
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                
                # Create log entry
                DashboardActivity.objects.create(
                    user=request.user,
                    action=action or "modified",
                    content_type=content_type or "Content",
                    object_id=object_id,
                    object_str=object_str,
                    ip_address=ip
                )
            
            return response
        return wrapper
    return decorator


def get_user_preferences(request):
    """Get or create dashboard preferences for the current user"""
    if request.user.is_authenticated:
        prefs, created = DashboardUserPreference.objects.get_or_create(user=request.user)
        return prefs
    return None


def apply_user_preferences(request, context):
    """Apply user preferences to the context dictionary"""
    prefs = get_user_preferences(request)
    if prefs:
        context.update({
            'user_preferences': prefs,
            'items_per_page': prefs.items_per_page,
            'default_view': prefs.default_view,
            'color_theme': prefs.color_theme,
        })
    return context