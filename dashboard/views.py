# dashboard/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse

from bakeshop.models import (
    SiteSettings, HomeSection, HomeBanner, 
    AboutSection, TeamMember, Award, Timeline,
    CareerSection, JobCategory, JobPosition, EmployeeTestimonial, Benefit,
    FranchiseSection, FranchiseModel, FranchiseeTestimonial, FAQ, InvestmentBreakdown, ProcessStep,
    StoreLocation, LocationStat,
    MenuCategory, MenuItem, FeaturedItem, SpecialOffer,
    GalleryImage, ContactMessage
)

from .forms import (
    SiteSettingsForm, HomeSectionForm, HomeBannerForm, 
    AboutSectionForm, TeamMemberForm, AwardForm, TimelineForm,
    CareerSectionForm, JobCategoryForm, JobPositionForm, EmployeeTestimonialForm, BenefitForm,
    FranchiseSectionForm, FranchiseModelForm, FranchiseeTestimonialForm, FAQForm, InvestmentBreakdownForm, ProcessStepForm,
    StoreLocationForm, LocationStatForm,
    MenuCategoryForm, MenuItemForm, FeaturedItemForm, SpecialOfferForm,
    GalleryImageForm
)


# Helper function to get site settings
def get_site_settings():
    return SiteSettings.objects.first() or SiteSettings.objects.create(site_name="Bakeshop")


# Dashboard Home
@login_required
def dashboard_home(request):
    site_settings = get_site_settings()
    
    # Dashboard statistics
    stats = {
        'locations': StoreLocation.objects.filter(is_active=True).count(),
        'menu_items': MenuItem.objects.filter(is_active=True).count(),
        'jobs': JobPosition.objects.filter(is_active=True).count(),
        'messages': ContactMessage.objects.filter(is_read=False).count()
    }
    
    # Recent messages
    recent_messages = ContactMessage.objects.all().order_by('-date_submitted')[:5]
    
    # Upcoming special offers
    special_offers = SpecialOffer.objects.filter(is_active=True).order_by('expiry_date')[:5]
    
    context = {
        'active_page': 'dashboard',
        'site_settings': site_settings,
        'stats': stats,
        'recent_messages': recent_messages,
        'special_offers': special_offers
    }
    
    return render(request, 'dashboard/index.html', context)


# Home Page Management
@login_required
def manage_home(request):
    site_settings = get_site_settings()
    sections = HomeSection.objects.all().order_by('display_order')
    banners = HomeBanner.objects.all().order_by('display_order')
    gallery_images = GalleryImage.objects.filter(gallery_type='home').order_by('display_order')
    
    # Get the active tab from query parameters
    active_tab = request.GET.get('tab', 'sections')
    
    context = {
        'active_page': 'home',
        'site_settings': site_settings,
        'sections': sections,
        'banners': banners,
        'gallery_images': gallery_images,
        'active_tab': active_tab
    }
    
    return render(request, 'dashboard/home.html', context)


@login_required
def home_section_edit(request, section_id):
    site_settings = get_site_settings()
    section = get_object_or_404(HomeSection, id=section_id)
    
    if request.method == 'POST':
        form = HomeSectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, f'The "{section.title}" section has been updated successfully.')
            return redirect('dashboard:manage_home')
    else:
        form = HomeSectionForm(instance=section)
    
    context = {
        'active_page': 'home',
        'site_settings': site_settings,
        'section': section,
        'form': form
    }
    
    return render(request, 'dashboard/home_section_edit.html', context)


@login_required
def home_banner_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = HomeBannerForm(request.POST, request.FILES)
        if form.is_valid():
            banner = form.save()
            messages.success(request, f'The "{banner.title}" banner has been added successfully.')
            return redirect('dashboard:manage_home')
    else:
        form = HomeBannerForm()
    
    context = {
        'active_page': 'home',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/home_banner_form.html', context)


@login_required
def home_banner_edit(request, banner_id):
    site_settings = get_site_settings()
    banner = get_object_or_404(HomeBanner, id=banner_id)
    
    if request.method == 'POST':
        form = HomeBannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, f'The "{banner.title}" banner has been updated successfully.')
            return redirect('dashboard:manage_home')
    else:
        form = HomeBannerForm(instance=banner)
    
    context = {
        'active_page': 'home',
        'site_settings': site_settings,
        'banner': banner,
        'form': form
    }
    
    return render(request, 'dashboard/home_banner_form.html', context)


@login_required
def home_banner_delete(request, banner_id):
    site_settings = get_site_settings()
    banner = get_object_or_404(HomeBanner, id=banner_id)
    
    if request.method == 'POST':
        banner.delete()
        messages.success(request, f'The "{banner.title}" banner has been deleted successfully.')
        return redirect('dashboard:manage_home')
    
    context = {
        'active_page': 'home',
        'site_settings': site_settings,
        'banner': banner
    }
    
    return render(request, 'dashboard/home_banner_delete.html', context)


# About Page Management
@login_required
def manage_about(request):
    site_settings = get_site_settings()
    sections = AboutSection.objects.all().order_by('section_type')
    team_members = TeamMember.objects.all().order_by('display_order')
    awards = Award.objects.all().order_by('-year')
    timeline_events = Timeline.objects.all().order_by('-year')
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'sections': sections,
        'team_members': team_members,
        'awards': awards,
        'timeline_events': timeline_events
    }
    
    return render(request, 'dashboard/about.html', context)


@login_required
def about_section_edit(request, section_id):
    site_settings = get_site_settings()
    section = get_object_or_404(AboutSection, id=section_id)
    
    if request.method == 'POST':
        form = AboutSectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, f'The "{section.title}" section has been updated successfully.')
            return redirect('dashboard:manage_about')
    else:
        form = AboutSectionForm(instance=section)
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'section': section,
        'form': form
    }
    
    return render(request, 'dashboard/about_section_edit.html', context)


@login_required
def team_member_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save()
            messages.success(request, f'Team member "{member.name}" has been added successfully.')
            return redirect('dashboard:manage_about')
    else:
        form = TeamMemberForm()
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/team_member_form.html', context)


@login_required
def team_member_edit(request, member_id):
    site_settings = get_site_settings()
    member = get_object_or_404(TeamMember, id=member_id)
    
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, f'Team member "{member.name}" has been updated successfully.')
            return redirect('dashboard:manage_about')
    else:
        form = TeamMemberForm(instance=member)
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'member': member,
        'form': form
    }
    
    return render(request, 'dashboard/team_member_form.html', context)


@login_required
def team_member_delete(request, member_id):
    site_settings = get_site_settings()
    member = get_object_or_404(TeamMember, id=member_id)
    
    if request.method == 'POST':
        member.delete()
        messages.success(request, f'Team member "{member.name}" has been deleted successfully.')
        return redirect('dashboard:manage_about')
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'member': member
    }
    
    return render(request, 'dashboard/team_member_delete.html', context)


@login_required
def award_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            award = form.save()
            messages.success(request, f'Award "{award.title}" has been added successfully.')
            return redirect('dashboard:manage_about')
    else:
        form = AwardForm()
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/award_form.html', context)


@login_required
def award_edit(request, award_id):
    site_settings = get_site_settings()
    award = get_object_or_404(Award, id=award_id)
    
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES, instance=award)
        if form.is_valid():
            form.save()
            messages.success(request, f'Award "{award.title}" has been updated successfully.')
            return redirect('dashboard:manage_about')
    else:
        form = AwardForm(instance=award)
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'award': award,
        'form': form
    }
    
    return render(request, 'dashboard/award_form.html', context)


@login_required
def award_delete(request, award_id):
    site_settings = get_site_settings()
    award = get_object_or_404(Award, id=award_id)
    
    if request.method == 'POST':
        award.delete()
        messages.success(request, f'Award "{award.title}" has been deleted successfully.')
        return redirect('dashboard:manage_about')
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'award': award
    }
    
    return render(request, 'dashboard/award_delete.html', context)


@login_required
def timeline_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = TimelineForm(request.POST)
        if form.is_valid():
            timeline = form.save()
            messages.success(request, f'Timeline event "{timeline.title}" has been added successfully.')
            return redirect('dashboard:manage_about')
    else:
        form = TimelineForm()
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/timeline_form.html', context)


@login_required
def timeline_edit(request, timeline_id):
    site_settings = get_site_settings()
    timeline = get_object_or_404(Timeline, id=timeline_id)
    
    if request.method == 'POST':
        form = TimelineForm(request.POST, instance=timeline)
        if form.is_valid():
            form.save()
            messages.success(request, f'Timeline event "{timeline.title}" has been updated successfully.')
            return redirect('dashboard:manage_about')
    else:
        form = TimelineForm(instance=timeline)
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'timeline': timeline,
        'form': form
    }
    
    return render(request, 'dashboard/timeline_form.html', context)


@login_required
def timeline_delete(request, timeline_id):
    site_settings = get_site_settings()
    timeline = get_object_or_404(Timeline, id=timeline_id)
    
    if request.method == 'POST':
        timeline.delete()
        messages.success(request, f'Timeline event "{timeline.title}" has been deleted successfully.')
        return redirect('dashboard:manage_about')
    
    context = {
        'active_page': 'about',
        'site_settings': site_settings,
        'timeline': timeline
    }
    
    return render(request, 'dashboard/timeline_delete.html', context)


# Menu Page Management
@login_required
def manage_menu(request):
    site_settings = get_site_settings()
    categories = MenuCategory.objects.all().order_by('display_order')
    menu_items = MenuItem.objects.all().order_by('category', 'display_order')
    featured_items = FeaturedItem.objects.all().order_by('display_order')
    special_offers = SpecialOffer.objects.all().order_by('-is_active', 'expiry_date')
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'categories': categories,
        'menu_items': menu_items,
        'featured_items': featured_items,
        'special_offers': special_offers
    }
    
    return render(request, 'dashboard/menu.html', context)


@login_required
def menu_category_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = MenuCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Category "{category.name}" has been added successfully.')
            return redirect('dashboard:manage_menu')
    else:
        form = MenuCategoryForm()
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/menu_category_form.html', context)


@login_required
def menu_category_edit(request, category_id):
    site_settings = get_site_settings()
    category = get_object_or_404(MenuCategory, id=category_id)
    
    if request.method == 'POST':
        form = MenuCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Category "{category.name}" has been updated successfully.')
            return redirect('dashboard:manage_menu')
    else:
        form = MenuCategoryForm(instance=category)
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'category': category,
        'form': form
    }
    
    return render(request, 'dashboard/menu_category_form.html', context)


@login_required
def menu_category_delete(request, category_id):
    site_settings = get_site_settings()
    category = get_object_or_404(MenuCategory, id=category_id)
    
    if request.method == 'POST':
        category.delete()
        messages.success(request, f'Category "{category.name}" has been deleted successfully.')
        return redirect('dashboard:manage_menu')
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'category': category
    }
    
    return render(request, 'dashboard/menu_category_delete.html', context)


@login_required
def menu_item_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, f'Menu item "{item.name}" has been added successfully.')
            return redirect('dashboard:manage_menu')
    else:
        form = MenuItemForm()
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/menu_item_form.html', context)


@login_required
def menu_item_edit(request, item_id):
    site_settings = get_site_settings()
    item = get_object_or_404(MenuItem, id=item_id)
    
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Menu item "{item.name}" has been updated successfully.')
            return redirect('dashboard:manage_menu')
    else:
        form = MenuItemForm(instance=item)
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'item': item,
        'form': form
    }
    
    return render(request, 'dashboard/menu_item_form.html', context)


@login_required
def menu_item_delete(request, item_id):
    site_settings = get_site_settings()
    item = get_object_or_404(MenuItem, id=item_id)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, f'Menu item "{item.name}" has been deleted successfully.')
        return redirect('dashboard:manage_menu')
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'item': item
    }
    
    return render(request, 'dashboard/menu_item_delete.html', context)


@login_required
def featured_item_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = FeaturedItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, f'Featured item "{item.title}" has been added successfully.')
            return redirect('dashboard:manage_menu')
    else:
        form = FeaturedItemForm()
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/featured_item_form.html', context)


@login_required
def featured_item_edit(request, featured_id):
    site_settings = get_site_settings()
    item = get_object_or_404(FeaturedItem, id=featured_id)
    
    if request.method == 'POST':
        form = FeaturedItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Featured item "{item.title}" has been updated successfully.')
            return redirect('dashboard:manage_menu')
    else:
        form = FeaturedItemForm(instance=item)
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'item': item,
        'form': form
    }
    
    return render(request, 'dashboard/featured_item_form.html', context)


@login_required
def featured_item_delete(request, featured_id):
    site_settings = get_site_settings()
    item = get_object_or_404(FeaturedItem, id=featured_id)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, f'Featured item "{item.title}" has been deleted successfully.')
        return redirect('dashboard:manage_menu')
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'item': item
    }
    
    return render(request, 'dashboard/featured_item_delete.html', context)


@login_required
def special_offer_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = SpecialOfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = form.save()
            messages.success(request, f'Special offer "{offer.title}" has been added successfully.')
            return redirect('dashboard:manage_menu')
    else:
        form = SpecialOfferForm()
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/special_offer_form.html', context)


@login_required
def special_offer_edit(request, offer_id):
    site_settings = get_site_settings()
    offer = get_object_or_404(SpecialOffer, id=offer_id)
    
    if request.method == 'POST':
        form = SpecialOfferForm(request.POST, request.FILES, instance=offer)
        if form.is_valid():
            form.save()
            messages.success(request, f'Special offer "{offer.title}" has been updated successfully.')
            return redirect('dashboard:manage_menu')
    else:
        form = SpecialOfferForm(instance=offer)
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'offer': offer,
        'form': form
    }
    
    return render(request, 'dashboard/special_offer_form.html', context)


@login_required
def special_offer_delete(request, offer_id):
    site_settings = get_site_settings()
    offer = get_object_or_404(SpecialOffer, id=offer_id)
    
    if request.method == 'POST':
        offer.delete()
        messages.success(request, f'Special offer "{offer.title}" has been deleted successfully.')
        return redirect('dashboard:manage_menu')
    
    context = {
        'active_page': 'menu',
        'site_settings': site_settings,
        'offer': offer
    }
    
    return render(request, 'dashboard/special_offer_delete.html', context)


# Career Page Management
@login_required
def manage_career(request):
    site_settings = get_site_settings()
    sections = CareerSection.objects.all().order_by('section_type')
    categories = JobCategory.objects.all().order_by('display_order')
    positions = JobPosition.objects.all().order_by('category', 'display_order')
    benefits = Benefit.objects.all().order_by('display_order')
    testimonials = EmployeeTestimonial.objects.all().order_by('display_order')
    process_steps = ProcessStep.objects.filter(process_type='career').order_by('step_number')
    
    # Add position count to categories
    for category in categories:
        category.position_count = positions.filter(category=category, is_active=True).count()
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'sections': sections,
        'categories': categories,
        'positions': positions,
        'benefits': benefits,
        'testimonials': testimonials,
        'process_steps': process_steps
    }
    
    return render(request, 'dashboard/career.html', context)


@login_required
def career_section_edit(request, section_id):
    site_settings = get_site_settings()
    section = get_object_or_404(CareerSection, id=section_id)
    
    if request.method == 'POST':
        form = CareerSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, f'The "{section.title}" section has been updated successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = CareerSectionForm(instance=section)
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'section': section,
        'form': form
    }
    
    return render(request, 'dashboard/career_section_edit.html', context)


@login_required
def job_category_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = JobCategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Job category "{category.name}" has been added successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = JobCategoryForm()
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/job_category_form.html', context)


@login_required
def job_category_edit(request, category_id):
    site_settings = get_site_settings()
    category = get_object_or_404(JobCategory, id=category_id)
    
    if request.method == 'POST':
        form = JobCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Job category "{category.name}" has been updated successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = JobCategoryForm(instance=category)
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'category': category,
        'form': form
    }
    
    return render(request, 'dashboard/job_category_form.html', context)


@login_required
def job_category_delete(request, category_id):
    site_settings = get_site_settings()
    category = get_object_or_404(JobCategory, id=category_id)
    
    if request.method == 'POST':
        category.delete()
        messages.success(request, f'Job category "{category.name}" has been deleted successfully.')
        return redirect('dashboard:manage_career')
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'category': category
    }
    
    return render(request, 'dashboard/job_category_delete.html', context)


@login_required
def job_position_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = JobPositionForm(request.POST)
        if form.is_valid():
            position = form.save()
            messages.success(request, f'Job position "{position.title}" has been added successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = JobPositionForm()
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/job_position_form.html', context)


@login_required
def job_position_edit(request, position_id):
    site_settings = get_site_settings()
    position = get_object_or_404(JobPosition, id=position_id)
    
    if request.method == 'POST':
        form = JobPositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            messages.success(request, f'Job position "{position.title}" has been updated successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = JobPositionForm(instance=position)
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'position': position,
        'form': form
    }
    
    return render(request, 'dashboard/job_position_form.html', context)


@login_required
def job_position_delete(request, position_id):
    site_settings = get_site_settings()
    position = get_object_or_404(JobPosition, id=position_id)
    
    if request.method == 'POST':
        position.delete()
        messages.success(request, f'Job position "{position.title}" has been deleted successfully.')
        return redirect('dashboard:manage_career')
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'position': position
    }
    
    return render(request, 'dashboard/job_position_delete.html', context)


@login_required
def employee_testimonial_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = EmployeeTestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save()
            messages.success(request, f'Employee testimonial from "{testimonial.name}" has been added successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = EmployeeTestimonialForm()
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/employee_testimonial_form.html', context)

# The file continues from line ~600 where it was cut off

@login_required
def employee_testimonial_edit(request, testimonial_id):
    site_settings = get_site_settings()
    testimonial = get_object_or_404(EmployeeTestimonial, id=testimonial_id)
    
    if request.method == 'POST':
        form = EmployeeTestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee testimonial from "{testimonial.name}" has been updated successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = EmployeeTestimonialForm(instance=testimonial)
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'testimonial': testimonial,
        'form': form
    }
    
    return render(request, 'dashboard/employee_testimonial_form.html', context)


@login_required
def employee_testimonial_delete(request, testimonial_id):
    site_settings = get_site_settings()
    testimonial = get_object_or_404(EmployeeTestimonial, id=testimonial_id)
    
    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, f'Employee testimonial from "{testimonial.name}" has been deleted successfully.')
        return redirect('dashboard:manage_career')
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'testimonial': testimonial
    }
    
    return render(request, 'dashboard/employee_testimonial_delete.html', context)


@login_required
def benefit_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = BenefitForm(request.POST)
        if form.is_valid():
            benefit = form.save()
            messages.success(request, f'Benefit "{benefit.title}" has been added successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = BenefitForm()
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/benefit_form.html', context)


@login_required
def benefit_edit(request, benefit_id):
    site_settings = get_site_settings()
    benefit = get_object_or_404(Benefit, id=benefit_id)
    
    if request.method == 'POST':
        form = BenefitForm(request.POST, instance=benefit)
        if form.is_valid():
            form.save()
            messages.success(request, f'Benefit "{benefit.title}" has been updated successfully.')
            return redirect('dashboard:manage_career')
    else:
        form = BenefitForm(instance=benefit)
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'benefit': benefit,
        'form': form
    }
    
    return render(request, 'dashboard/benefit_form.html', context)


@login_required
def benefit_delete(request, benefit_id):
    site_settings = get_site_settings()
    benefit = get_object_or_404(Benefit, id=benefit_id)
    
    if request.method == 'POST':
        benefit.delete()
        messages.success(request, f'Benefit "{benefit.title}" has been deleted successfully.')
        return redirect('dashboard:manage_career')
    
    context = {
        'active_page': 'career',
        'site_settings': site_settings,
        'benefit': benefit
    }
    
    return render(request, 'dashboard/benefit_delete.html', context)


# Franchise Page Management
@login_required
def manage_franchise(request):
    site_settings = get_site_settings()
    sections = FranchiseSection.objects.all().order_by('section_type')
    models = FranchiseModel.objects.all().order_by('display_order')
    testimonials = FranchiseeTestimonial.objects.all().order_by('display_order')
    faqs = FAQ.objects.filter(category='franchise').order_by('display_order')
    investments = InvestmentBreakdown.objects.all().order_by('display_order')
    process_steps = ProcessStep.objects.filter(process_type='franchise').order_by('step_number')
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'sections': sections,
        'models': models,
        'testimonials': testimonials,
        'faqs': faqs,
        'investments': investments,
        'process_steps': process_steps
    }
    
    return render(request, 'dashboard/franchise.html', context)


@login_required
def franchise_section_edit(request, section_id):
    site_settings = get_site_settings()
    section = get_object_or_404(FranchiseSection, id=section_id)
    
    if request.method == 'POST':
        form = FranchiseSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, f'The "{section.title}" section has been updated successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = FranchiseSectionForm(instance=section)
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'section': section,
        'form': form
    }
    
    return render(request, 'dashboard/franchise_section_edit.html', context)


@login_required
def franchise_model_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = FranchiseModelForm(request.POST)
        if form.is_valid():
            model = form.save()
            messages.success(request, f'Franchise model "{model.name}" has been added successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = FranchiseModelForm()
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/franchise_model_form.html', context)


@login_required
def franchise_model_edit(request, model_id):
    site_settings = get_site_settings()
    model = get_object_or_404(FranchiseModel, id=model_id)
    
    if request.method == 'POST':
        form = FranchiseModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            messages.success(request, f'Franchise model "{model.name}" has been updated successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = FranchiseModelForm(instance=model)
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'model': model,
        'form': form
    }
    
    return render(request, 'dashboard/franchise_model_form.html', context)


@login_required
def franchise_model_delete(request, model_id):
    site_settings = get_site_settings()
    model = get_object_or_404(FranchiseModel, id=model_id)
    
    if request.method == 'POST':
        model.delete()
        messages.success(request, f'Franchise model "{model.name}" has been deleted successfully.')
        return redirect('dashboard:manage_franchise')
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'model': model
    }
    
    return render(request, 'dashboard/franchise_model_delete.html', context)


@login_required
def franchisee_testimonial_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = FranchiseeTestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save()
            messages.success(request, f'Franchisee testimonial from "{testimonial.name}" has been added successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = FranchiseeTestimonialForm()
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/franchisee_testimonial_form.html', context)


@login_required
def franchisee_testimonial_edit(request, testimonial_id):
    site_settings = get_site_settings()
    testimonial = get_object_or_404(FranchiseeTestimonial, id=testimonial_id)
    
    if request.method == 'POST':
        form = FranchiseeTestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, f'Franchisee testimonial from "{testimonial.name}" has been updated successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = FranchiseeTestimonialForm(instance=testimonial)
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'testimonial': testimonial,
        'form': form
    }
    
    return render(request, 'dashboard/franchisee_testimonial_form.html', context)


@login_required
def franchisee_testimonial_delete(request, testimonial_id):
    site_settings = get_site_settings()
    testimonial = get_object_or_404(FranchiseeTestimonial, id=testimonial_id)
    
    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, f'Franchisee testimonial from "{testimonial.name}" has been deleted successfully.')
        return redirect('dashboard:manage_franchise')
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'testimonial': testimonial
    }
    
    return render(request, 'dashboard/franchisee_testimonial_delete.html', context)


@login_required
def faq_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save()
            messages.success(request, f'FAQ "{faq.question}" has been added successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = FAQForm(initial={'category': 'franchise'})
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/faq_form.html', context)


@login_required
def faq_edit(request, faq_id):
    site_settings = get_site_settings()
    faq = get_object_or_404(FAQ, id=faq_id)
    
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, f'FAQ "{faq.question}" has been updated successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = FAQForm(instance=faq)
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'faq': faq,
        'form': form
    }
    
    return render(request, 'dashboard/faq_form.html', context)


@login_required
def faq_delete(request, faq_id):
    site_settings = get_site_settings()
    faq = get_object_or_404(FAQ, id=faq_id)
    
    if request.method == 'POST':
        faq.delete()
        messages.success(request, f'FAQ "{faq.question}" has been deleted successfully.')
        return redirect('dashboard:manage_franchise')
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'faq': faq
    }
    
    return render(request, 'dashboard/faq_delete.html', context)


@login_required
def investment_breakdown_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = InvestmentBreakdownForm(request.POST)
        if form.is_valid():
            item = form.save()
            messages.success(request, f'Investment component "{item.component}" has been added successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = InvestmentBreakdownForm()
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/investment_breakdown_form.html', context)


@login_required
def investment_breakdown_edit(request, item_id):
    site_settings = get_site_settings()
    item = get_object_or_404(InvestmentBreakdown, id=item_id)
    
    if request.method == 'POST':
        form = InvestmentBreakdownForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Investment component "{item.component}" has been updated successfully.')
            return redirect('dashboard:manage_franchise')
    else:
        form = InvestmentBreakdownForm(instance=item)
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'item': item,
        'form': form
    }
    
    return render(request, 'dashboard/investment_breakdown_form.html', context)


@login_required
def investment_breakdown_delete(request, item_id):
    site_settings = get_site_settings()
    item = get_object_or_404(InvestmentBreakdown, id=item_id)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, f'Investment component "{item.component}" has been deleted successfully.')
        return redirect('dashboard:manage_franchise')
    
    context = {
        'active_page': 'franchise',
        'site_settings': site_settings,
        'item': item
    }
    
    return render(request, 'dashboard/investment_breakdown_delete.html', context)


# Process steps management (shared by career and franchise pages)
@login_required
def process_step_add(request):
    site_settings = get_site_settings()
    
    # Determine the process type based on query parameter
    process_type = request.GET.get('type', 'career')
    
    if request.method == 'POST':
        form = ProcessStepForm(request.POST)
        if form.is_valid():
            step = form.save()
            messages.success(request, f'Process step "{step.title}" has been added successfully.')
            
            # Redirect based on process type
            if step.process_type == 'career':
                return redirect('dashboard:manage_career')
            else:
                return redirect('dashboard:manage_franchise')
    else:
        form = ProcessStepForm(initial={'process_type': process_type})
    
    context = {
        'active_page': 'career' if process_type == 'career' else 'franchise',
        'site_settings': site_settings,
        'form': form,
        'process_type': process_type
    }
    
    return render(request, 'dashboard/process_step_form.html', context)


@login_required
def process_step_edit(request, step_id):
    site_settings = get_site_settings()
    step = get_object_or_404(ProcessStep, id=step_id)
    
    if request.method == 'POST':
        form = ProcessStepForm(request.POST, instance=step)
        if form.is_valid():
            form.save()
            messages.success(request, f'Process step "{step.title}" has been updated successfully.')
            
            # Redirect based on process type
            if step.process_type == 'career':
                return redirect('dashboard:manage_career')
            else:
                return redirect('dashboard:manage_franchise')
    else:
        form = ProcessStepForm(instance=step)
    
    context = {
        'active_page': 'career' if step.process_type == 'career' else 'franchise',
        'site_settings': site_settings,
        'step': step,
        'form': form
    }
    
    return render(request, 'dashboard/process_step_form.html', context)


@login_required
def process_step_delete(request, step_id):
    site_settings = get_site_settings()
    step = get_object_or_404(ProcessStep, id=step_id)
    process_type = step.process_type  # Save for redirect
    
    if request.method == 'POST':
        step.delete()
        messages.success(request, f'Process step "{step.title}" has been deleted successfully.')
        
        # Redirect based on process type
        if process_type == 'career':
            return redirect('dashboard:manage_career')
        else:
            return redirect('dashboard:manage_franchise')
    
    context = {
        'active_page': 'career' if process_type == 'career' else 'franchise',
        'site_settings': site_settings,
        'step': step
    }
    
    return render(request, 'dashboard/process_step_delete.html', context)


# Location Management
@login_required
def manage_location(request):
    site_settings = get_site_settings()
    locations = StoreLocation.objects.all().order_by('city', 'name')
    stats = LocationStat.objects.all().order_by('display_order')
    
    context = {
        'active_page': 'location',
        'site_settings': site_settings,
        'locations': locations,
        'stats': stats
    }
    
    return render(request, 'dashboard/location.html', context)


@login_required
def store_location_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = StoreLocationForm(request.POST, request.FILES)
        if form.is_valid():
            location = form.save()
            messages.success(request, f'Location "{location.name}" has been added successfully.')
            return redirect('dashboard:manage_location')
    else:
        form = StoreLocationForm()
    
    context = {
        'active_page': 'location',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/store_location_form.html', context)


@login_required
def store_location_edit(request, location_id):
    site_settings = get_site_settings()
    location = get_object_or_404(StoreLocation, id=location_id)
    
    if request.method == 'POST':
        form = StoreLocationForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, f'Location "{location.name}" has been updated successfully.')
            return redirect('dashboard:manage_location')
    else:
        form = StoreLocationForm(instance=location)
    
    context = {
        'active_page': 'location',
        'site_settings': site_settings,
        'location': location,
        'form': form
    }
    
    return render(request, 'dashboard/store_location_form.html', context)


@login_required
def store_location_delete(request, location_id):
    site_settings = get_site_settings()
    location = get_object_or_404(StoreLocation, id=location_id)
    
    if request.method == 'POST':
        location.delete()
        messages.success(request, f'Location "{location.name}" has been deleted successfully.')
        return redirect('dashboard:manage_location')
    
    context = {
        'active_page': 'location',
        'site_settings': site_settings,
        'location': location
    }
    
    return render(request, 'dashboard/store_location_delete.html', context)


@login_required
def location_stat_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = LocationStatForm(request.POST)
        if form.is_valid():
            stat = form.save()
            messages.success(request, f'Statistic "{stat.label}" has been added successfully.')
            return redirect('dashboard:manage_location')
    else:
        form = LocationStatForm()
    
    context = {
        'active_page': 'location',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/location_stat_form.html', context)


@login_required
def location_stat_edit(request, stat_id):
    site_settings = get_site_settings()
    stat = get_object_or_404(LocationStat, id=stat_id)
    
    if request.method == 'POST':
        form = LocationStatForm(request.POST, instance=stat)
        if form.is_valid():
            form.save()
            messages.success(request, f'Statistic "{stat.label}" has been updated successfully.')
            return redirect('dashboard:manage_location')
    else:
        form = LocationStatForm(instance=stat)
    
    context = {
        'active_page': 'location',
        'site_settings': site_settings,
        'stat': stat,
        'form': form
    }
    
    return render(request, 'dashboard/location_stat_form.html', context)


@login_required
def location_stat_delete(request, stat_id):
    site_settings = get_site_settings()
    stat = get_object_or_404(LocationStat, id=stat_id)
    
    if request.method == 'POST':
        stat.delete()
        messages.success(request, f'Statistic "{stat.label}" has been deleted successfully.')
        return redirect('dashboard:manage_location')
    
    context = {
        'active_page': 'location',
        'site_settings': site_settings,
        'stat': stat
    }
    
    return render(request, 'dashboard/location_stat_delete.html', context)


# Gallery image management
@login_required
def gallery_image_add(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            messages.success(request, f'Gallery image "{image.title}" has been added successfully.')
            return redirect('dashboard:manage_home')
    else:
        form = GalleryImageForm()
    
    context = {
        'active_page': 'home',
        'site_settings': site_settings,
        'form': form
    }
    
    return render(request, 'dashboard/gallery_image_form.html', context)


@login_required
def gallery_image_edit(request, image_id):
    site_settings = get_site_settings()
    image = get_object_or_404(GalleryImage, id=image_id)
    
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, f'Gallery image "{image.title}" has been updated successfully.')
            return redirect('dashboard:manage_home')
    else:
        form = GalleryImageForm(instance=image)
    
    context = {
        'active_page': 'home',
        'site_settings': site_settings,
        'image': image,
        'form': form
    }
    
    return render(request, 'dashboard/gallery_image_form.html', context)


@login_required
def gallery_image_delete(request, image_id):
    site_settings = get_site_settings()
    image = get_object_or_404(GalleryImage, id=image_id)
    
    if request.method == 'POST':
        image.delete()
        messages.success(request, f'Gallery image "{image.title}" has been deleted successfully.')
        return redirect('dashboard:manage_home')
    
    context = {
        'active_page': 'home',
        'site_settings': site_settings,
        'image': image
    }
    
    return render(request, 'dashboard/gallery_image_delete.html', context)


# Contact Messages
@login_required
def contact_messages(request):
    site_settings = get_site_settings()
    
    # Filter messages based on query parameter
    filter_param = request.GET.get('filter', 'all')
    
    if filter_param == 'unread':
        messages_list = ContactMessage.objects.filter(is_read=False).order_by('-date_submitted')
    elif filter_param == 'read':
        messages_list = ContactMessage.objects.filter(is_read=True).order_by('-date_submitted')
    else:
        messages_list = ContactMessage.objects.all().order_by('-date_submitted')
    
    # Pagination
    paginator = Paginator(messages_list, 10)  # Show 10 messages per page
    page = request.GET.get('page')
    
    try:
        messages_page = paginator.page(page)
    except PageNotAnInteger:
        messages_page = paginator.page(1)
    except EmptyPage:
        messages_page = paginator.page(paginator.num_pages)
    
    context = {
        'active_page': 'messages',
        'site_settings': site_settings,
        'messages_page': messages_page,
        'filter': filter_param
    }
    
    return render(request, 'dashboard/contact_messages.html', context)


@login_required
def contact_message_detail(request, message_id):
    site_settings = get_site_settings()
    message = get_object_or_404(ContactMessage, id=message_id)
    
    # Mark as read when viewed
    if not message.is_read:
        message.is_read = True
        message.save()
    
    context = {
        'active_page': 'messages',
        'site_settings': site_settings,
        'message': message
    }
    
    return render(request, 'dashboard/contact_message_detail.html', context)


@login_required
def mark_message_as_read(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    message.is_read = not message.is_read  # Toggle read status
    message.save()
    
    # Determine redirect URL
    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return redirect('dashboard:contact_messages')


@login_required
def contact_message_delete(request, message_id):
    site_settings = get_site_settings()
    message = get_object_or_404(ContactMessage, id=message_id)
    
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'The message has been deleted successfully.')
        return redirect('dashboard:contact_messages')
    
    context = {
        'active_page': 'messages',
        'site_settings': site_settings,
        'message': message
    }
    
    return render(request, 'dashboard/contact_message_delete.html', context)


# Site Settings
@login_required
def site_settings(request):
    settings = get_site_settings()
    
    if request.method == 'POST':
        form = SiteSettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Site settings have been updated successfully.')
            return redirect('dashboard:site_settings')
    else:
        form = SiteSettingsForm(instance=settings)
    
    context = {
        'active_page': 'settings',
        'site_settings': settings,
        'settings': settings,  # For template rendering
        'form': form
    }
    
    return render(request, 'dashboard/site_settings.html', context)