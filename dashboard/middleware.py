# dashboard/middleware.py

from django.utils.deprecation import MiddlewareMixin
from dashboard.models import DashboardActivity
import re

class DashboardActivityMiddleware(MiddlewareMixin):
    """Middleware to log dashboard actions automatically"""
    
    # Actions to log based on URL patterns
    ACTION_PATTERNS = [
        (r'add/$', 'created'),
        (r'edit/\d+/$', 'updated'),
        (r'delete/\d+/$', 'deleted'),
        (r'mark-as-read/\d+/$', 'marked as read'),
    ]
    
    # Map URL segments to content types
    CONTENT_TYPE_MAP = {
        'banner': 'Home Banner',
        'section': 'Content Section',
        'team': 'Team Member',
        'award': 'Award',
        'timeline': 'Timeline Event',
        'menu/category': 'Menu Category',
        'menu/item': 'Menu Item',
        'menu/featured': 'Featured Item',
        'menu/offer': 'Special Offer',
        'career/category': 'Job Category',
        'career/position': 'Job Position',
        'career/testimonial': 'Employee Testimonial',
        'career/benefit': 'Employee Benefit',
        'franchise/model': 'Franchise Model',
        'franchise/testimonial': 'Franchisee Testimonial',
        'franchise/faq': 'FAQ',
        'franchise/investment': 'Investment Breakdown',
        'location': 'Store Location',
        'location/stat': 'Location Statistic',
        'process': 'Process Step',
        'gallery': 'Gallery Image',
        'messages': 'Contact Message',
        'settings': 'Site Settings',
    }
    
    def process_response(self, request, response):
        # Only log POST requests from authenticated users to dashboard URLs
        if (request.method == 'POST' and 
                request.user.is_authenticated and 
                'dashboard' in request.path and
                response.status_code in [200, 301, 302]):
            
            # Skip certain URLs
            if 'login' in request.path or 'logout' in request.path:
                return response
                
            # Determine the action and content type from the URL
            action = 'modified'  # Default action
            content_type = 'content'  # Default type
            object_id = None
            object_str = 'content'
            
            # Extract path without query string
            path = request.path.split('?')[0]
            
            # Try to determine action from URL pattern
            for pattern, act in self.ACTION_PATTERNS:
                if re.search(pattern, path):
                    action = act
                    object_id = re.search(r'/(\d+)/', path)
                    if object_id:
                        object_id = int(object_id.group(1))
                    break
            
            # Try to determine content type from URL
            for key, content in self.CONTENT_TYPE_MAP.items():
                if key in path:
                    content_type = content
                    break
            
            # If we have form data, try to extract object name
            if hasattr(request, 'POST'):
                if 'title' in request.POST:
                    object_str = request.POST.get('title')[:255]
                elif 'name' in request.POST:
                    object_str = request.POST.get('name')[:255]
                elif 'question' in request.POST:
                    object_str = request.POST.get('question')[:255]
            
            # Create log entry
            DashboardActivity.objects.create(
                user=request.user,
                action=action,
                content_type=content_type,
                object_id=object_id,
                object_str=object_str,
                ip_address=self.get_client_ip(request)
            )
            
        return response
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip