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