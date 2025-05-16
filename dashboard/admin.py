# dashboard/admin.py

from django.contrib import admin
from dashboard.models import DashboardUserPreference, DashboardActivity
from bakeshop.models import (
    SiteSettings, HomeSection, HomeBanner, 
    AboutSection, TeamMember, Award, Timeline,
    CareerSection, JobCategory, JobPosition, EmployeeTestimonial, Benefit,
    FranchiseSection, FranchiseModel, FranchiseeTestimonial, FAQ, InvestmentBreakdown, ProcessStep,
    StoreLocation, LocationStat,
    MenuCategory, MenuItem, FeaturedItem, SpecialOffer,
    GalleryImage, ContactMessage
)

# Site Settings
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'phone_number', 'email')
    fieldsets = (
        ('General Information', {
            'fields': ('site_name', 'site_tagline', 'phone_number', 'email', 'address')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url')
        }),
        ('Footer', {
            'fields': ('footer_text',)
        }),
    )


# Home Page Admin
@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'display_order', 'is_active')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('display_order', 'is_active')


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    list_editable = ('display_order', 'is_active')


# About Page Admin
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'is_active')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'position', 'bio')
    list_editable = ('display_order', 'is_active')


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'year', 'display_order', 'is_active')
    list_filter = ('is_active', 'year')
    search_fields = ('title', 'organization', 'description')
    list_editable = ('display_order', 'is_active')


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')
    search_fields = ('title', 'description')
    ordering = ('-year',)


# Career Page Admin
@admin.register(CareerSection)
class CareerSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'is_active')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    list_editable = ('display_order', 'is_active')


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'employment_type', 'location', 'is_active', 'is_featured', 'is_urgent')
    list_filter = ('category', 'employment_type', 'is_active', 'is_featured', 'is_urgent')
    search_fields = ('title', 'description', 'responsibilities', 'requirements')
    list_editable = ('is_active', 'is_featured', 'is_urgent')


@admin.register(EmployeeTestimonial)
class EmployeeTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'years_at_company', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'position', 'testimonial')
    list_editable = ('display_order', 'is_active')


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order')
    search_fields = ('title', 'description')
    list_editable = ('display_order',)


# Franchise Page Admin
@admin.register(FranchiseSection)
class FranchiseSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'is_active')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)


@admin.register(FranchiseModel)
class FranchiseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'space_required', 'is_recommended', 'display_order', 'is_active')
    list_filter = ('is_recommended', 'is_active')
    search_fields = ('name', 'description', 'features')
    list_editable = ('display_order', 'is_active', 'is_recommended')


@admin.register(FranchiseeTestimonial)
class FranchiseeTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'years_as_franchisee', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'location', 'testimonial')
    list_editable = ('display_order', 'is_active')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'display_order')
    list_filter = ('category',)
    search_fields = ('question', 'answer')
    list_editable = ('display_order',)


@admin.register(InvestmentBreakdown)
class InvestmentBreakdownAdmin(admin.ModelAdmin):
    list_display = ('component', 'express_cost', 'standard_cost', 'premium_cost', 'display_order')
    search_fields = ('component',)
    list_editable = ('display_order',)


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'process_type', 'step_number')
    list_filter = ('process_type',)
    search_fields = ('title', 'description')
    list_editable = ('step_number',)


# Location Admin
@admin.register(StoreLocation)
class StoreLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'location_type', 'is_featured', 'is_coming_soon', 'is_active')
    list_filter = ('location_type', 'is_featured', 'is_coming_soon', 'is_active', 'state')
    search_fields = ('name', 'address', 'city', 'state', 'zip_code')
    list_editable = ('is_featured', 'is_coming_soon', 'is_active')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location_type', 'description', 'image')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state', 'zip_code', 'latitude', 'longitude')
        }),
        ('Contact', {
            'fields': ('phone', 'email')
        }),
        ('Hours', {
            'fields': ('monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 
                      'friday_hours', 'saturday_hours', 'sunday_hours', 'is_24hours')
        }),
        ('Status', {
            'fields': ('is_featured', 'is_coming_soon', 'is_active', 'rating')
        }),
    )


@admin.register(LocationStat)
class LocationStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'display_order')
    search_fields = ('label', 'value')
    list_editable = ('display_order',)


# Menu Admin
@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    list_editable = ('display_order', 'is_active')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_bestseller', 'is_new', 'is_seasonal', 'is_active')
    list_filter = ('category', 'is_vegetarian', 'is_gluten_free', 'is_sugar_free',
                  'is_bestseller', 'is_new', 'is_seasonal', 'is_active')
    search_fields = ('name', 'description', 'tags')
    list_editable = ('price', 'is_bestseller', 'is_new', 'is_seasonal', 'is_active')


@admin.register(FeaturedItem)
class FeaturedItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    list_editable = ('display_order', 'is_active')


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount_percentage', 'expiry_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    list_editable = ('is_active',)


# Gallery Admin
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'gallery_type', 'display_order', 'is_active')
    list_filter = ('gallery_type', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('display_order', 'is_active')


# Contact Messages Admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_submitted', 'is_read')
    list_filter = ('is_read', 'date_submitted')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date_submitted',)
    list_editable = ('is_read',)
    
    def has_add_permission(self, request):
        return False  # Prevent adding messages through admin


# Dashboard specific models
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