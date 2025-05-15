# bakeshop/signals.py

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import MenuItem, MenuCategory, ContactMessage, JobPosition


@receiver(pre_save, sender=MenuCategory)
def create_menu_category_slug(sender, instance, **kwargs):
    """
    Automatically generate slug for menu categories if not provided
    """
    if not instance.slug:
        instance.slug = slugify(instance.name)


@receiver(post_save, sender=MenuItem)
def update_category_status(sender, instance, **kwargs):
    """
    Ensure that a menu category is active if it has active items
    """
    category = instance.category
    
    # If the item is active and the category is not, activate the category
    if instance.is_active and not category.is_active:
        category.is_active = True
        category.save()


@receiver(post_save, sender=ContactMessage)
def send_notification_email(sender, instance, created, **kwargs):
    """
    Send notification email when a new message is received
    """
    if created:
        # This would be implemented with actual email sending code
        # For now it's just a placeholder for the signal
        pass


@receiver(post_save, sender=JobPosition)
def send_job_notification(sender, instance, created, **kwargs):
    """
    Send notification when a new job position is posted
    """
    if created and instance.is_active:
        # This would be implemented with actual notification code
        # For now it's just a placeholder for the signal
        pass