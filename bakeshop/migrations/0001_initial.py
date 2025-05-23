# Generated by Django 5.2.1 on 2025-05-16 01:34

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('section_type', models.CharField(choices=[('story', 'Our Story'), ('mission', 'Mission & Vision'), ('values', 'Core Values'), ('quality', 'Quality Commitment'), ('heritage', 'Heritage')], max_length=20)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/sections/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/awards/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-year', 'display_order'],
            },
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.CharField(help_text='Font Awesome class or icon name', max_length=50)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='CareerSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('section_type', models.CharField(choices=[('intro', 'Introduction'), ('culture', 'Company Culture'), ('benefits', 'Benefits'), ('growth', 'Career Growth'), ('process', 'Hiring Process')], max_length=20)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('is_franchise_inquiry', models.BooleanField(default=False)),
                ('investment_level', models.CharField(blank=True, max_length=50)),
                ('preferred_location', models.CharField(blank=True, max_length=100)),
                ('is_job_application', models.BooleanField(default=False)),
                ('position_applied', models.CharField(blank=True, max_length=100)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date_submitted'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('years_at_company', models.PositiveIntegerField()),
                ('testimonial', models.TextField()),
                ('image', models.ImageField(upload_to='career/testimonials/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('category', models.CharField(choices=[('general', 'General'), ('franchise', 'Franchise'), ('menu', 'Menu & Products'), ('order', 'Ordering')], max_length=20)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'ordering': ['category', 'display_order'],
            },
        ),
        migrations.CreateModel(
            name='FeaturedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='menu/featured/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='FranchiseeTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('years_as_franchisee', models.PositiveIntegerField()),
                ('testimonial', models.TextField()),
                ('image', models.ImageField(upload_to='franchise/testimonials/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='FranchiseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('space_required', models.CharField(max_length=100)),
                ('features', models.TextField()),
                ('is_recommended', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='FranchiseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('section_type', models.CharField(choices=[('intro', 'Introduction'), ('why', 'Why Franchise With Us'), ('requirements', 'Requirements'), ('support', 'Support & Training'), ('process', 'Application Process')], max_length=20)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('gallery_type', models.CharField(choices=[('about', 'About Us'), ('menu', 'Menu & Products'), ('location', 'Locations'), ('career', 'Career'), ('franchise', 'Franchise')], max_length=20)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['gallery_type', 'display_order'],
            },
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('image_desktop', models.ImageField(upload_to='home/banners/desktop/')),
                ('image_mobile', models.ImageField(blank=True, null=True, upload_to='home/banners/mobile/')),
                ('link_url', models.URLField(blank=True)),
                ('button_text', models.CharField(blank=True, max_length=50)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='HomeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('section_type', models.CharField(choices=[('welcome', 'Welcome'), ('about', 'About Us'), ('menu', 'Menu'), ('testimonial', 'Testimonial'), ('newsletter', 'Newsletter'), ('featured', 'Featured Products'), ('promo', 'Promotion')], max_length=20)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='home/sections/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='InvestmentBreakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.CharField(max_length=100)),
                ('express_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('standard_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('premium_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Job Categories',
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='LocationStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu/categories/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Menu Categories',
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_type', models.CharField(choices=[('career', 'Career Application'), ('franchise', 'Franchise Application')], max_length=20)),
                ('step_number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.CharField(blank=True, help_text='Font Awesome class or icon name', max_length=50)),
            ],
            options={
                'ordering': ['process_type', 'step_number'],
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('site_tagline', models.CharField(blank=True, max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='site/')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='site/')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('facebook_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('footer_text', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='menu/offers/')),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True)),
                ('expiry_date', models.DateField()),
            ],
            options={
                'ordering': ['expiry_date'],
            },
        ),
        migrations.CreateModel(
            name='StoreLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('location_type', models.CharField(choices=[('store', 'Retail Store'), ('express', 'Express Location'), ('cafe', 'Café & Dining')], max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='locations/')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('monday_hours', models.CharField(blank=True, max_length=100)),
                ('tuesday_hours', models.CharField(blank=True, max_length=100)),
                ('wednesday_hours', models.CharField(blank=True, max_length=100)),
                ('thursday_hours', models.CharField(blank=True, max_length=100)),
                ('friday_hours', models.CharField(blank=True, max_length=100)),
                ('saturday_hours', models.CharField(blank=True, max_length=100)),
                ('sunday_hours', models.CharField(blank=True, max_length=100)),
                ('is_24hours', models.BooleanField(default=False)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_coming_soon', models.BooleanField(default=False)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'ordering': ['city', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='about/team/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['year'],
            },
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('employment_type', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('contract', 'Contract'), ('temporary', 'Temporary'), ('internship', 'Internship')], max_length=20)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('responsibilities', ckeditor_uploader.fields.RichTextUploadingField()),
                ('requirements', ckeditor_uploader.fields.RichTextUploadingField()),
                ('benefits', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('salary_range', models.CharField(blank=True, max_length=100)),
                ('application_email', models.EmailField(max_length=254)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_urgent', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='bakeshop.jobcategory')),
            ],
            options={
                'ordering': ['-is_featured', '-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='menu/items/')),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('is_gluten_free', models.BooleanField(default=False)),
                ('is_sugar_free', models.BooleanField(default=False)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('is_seasonal', models.BooleanField(default=False)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('display_order', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bakeshop.menucategory')),
            ],
            options={
                'ordering': ['category__display_order', 'display_order'],
            },
        ),
    ]
