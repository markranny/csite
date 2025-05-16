document.addEventListener('DOMContentLoaded', function() {
    // Preloader
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        setTimeout(() => {
            preloader.classList.add('fade-out');
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 500);
        }, 500);
    }

    // Navigation toggle
    const navTrigger = document.querySelector('.nav-trigger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navTrigger && navMenu) {
        navTrigger.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // Banner slideshow functionality
    const setupBannerSlideshow = () => {
        const slides = document.querySelectorAll('.banner-slide');
        const dots = document.querySelectorAll('.banner-dot');
        const prevBtn = document.querySelector('.banner-arrow.prev');
        const nextBtn = document.querySelector('.banner-arrow.next');
        
        if (slides.length === 0) return;
        
        let currentSlide = 0;
        const slideCount = slides.length;
        
        // Auto slideshow
        let slideInterval = setInterval(nextSlide, 6000);
        
        function showSlide(n) {
            // Reset active class
            slides.forEach(slide => slide.classList.remove('active'));
            dots.forEach(dot => dot.classList.remove('active'));
            
            // Set current slide
            currentSlide = (n + slideCount) % slideCount;
            slides[currentSlide].classList.add('active');
            if (dots.length > 0) {
                dots[currentSlide].classList.add('active');
            }
            
            // Reset timer
            clearInterval(slideInterval);
            slideInterval = setInterval(nextSlide, 6000);
        }
        
        function nextSlide() {
            showSlide(currentSlide + 1);
        }
        
        function prevSlide() {
            showSlide(currentSlide - 1);
        }
        
        // Add event listeners
        if (prevBtn) prevBtn.addEventListener('click', prevSlide);
        if (nextBtn) nextBtn.addEventListener('click', nextSlide);
        
        // Add click events to dots
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => showSlide(index));
        });
    };
    
    // Initialize banner slideshow if present
    setupBannerSlideshow();

    // Testimonial slider functionality
    const setupTestimonialSlider = () => {
        const testimonialSlides = document.querySelectorAll('.testimonial-slide');
        const testimonialDots = document.querySelectorAll('.testimonial-dot');
        
        if (testimonialSlides.length === 0) return;
        
        let currentTestimonial = 0;
        const testimonialCount = testimonialSlides.length;
        
        // Auto testimonial rotation
        let testimonialInterval = setInterval(nextTestimonial, 5000);
        
        function showTestimonial(n) {
            // Reset active class
            testimonialSlides.forEach(slide => slide.classList.remove('active'));
            testimonialDots.forEach(dot => dot.classList.remove('active'));
            
            // Set current testimonial
            currentTestimonial = (n + testimonialCount) % testimonialCount;
            testimonialSlides[currentTestimonial].classList.add('active');
            testimonialDots[currentTestimonial].classList.add('active');
            
            // Reset timer
            clearInterval(testimonialInterval);
            testimonialInterval = setInterval(nextTestimonial, 5000);
        }
        
        function nextTestimonial() {
            showTestimonial(currentTestimonial + 1);
        }
        
        // Add click events to testimonial dots
        testimonialDots.forEach((dot, index) => {
            dot.addEventListener('click', () => showTestimonial(index));
        });
    };
    
    // Initialize testimonial slider if present
    setupTestimonialSlider();

    // Form validation
    const validateForm = (form) => {
        let isValid = true;
        const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        
        // Reset all error messages
        form.querySelectorAll('.text-danger').forEach(el => el.textContent = '');
        
        // Validate required fields
        form.querySelectorAll('[required]').forEach(field => {
            if (!field.value.trim()) {
                const errorElement = field.parentNode.querySelector('.text-danger') || 
                                    document.createElement('div');
                
                if (!field.parentNode.querySelector('.text-danger')) {
                    errorElement.classList.add('text-danger');
                    errorElement.style.fontSize = '14px';
                    errorElement.style.marginTop = '5px';
                    field.parentNode.appendChild(errorElement);
                }
                
                errorElement.textContent = `Please enter your ${field.placeholder || field.name}`;
                isValid = false;
            }
        });
        
        // Validate email fields
        form.querySelectorAll('input[type="email"]').forEach(field => {
            if (field.value.trim() && !emailRegex.test(field.value.trim())) {
                const errorElement = field.parentNode.querySelector('.text-danger') || 
                                    document.createElement('div');
                
                if (!field.parentNode.querySelector('.text-danger')) {
                    errorElement.classList.add('text-danger');
                    errorElement.style.fontSize = '14px';
                    errorElement.style.marginTop = '5px';
                    field.parentNode.appendChild(errorElement);
                }
                
                errorElement.textContent = 'Please enter a valid email address';
                isValid = false;
            }
        });
        
        return isValid;
    };
    
    // Apply validation to all forms
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', (e) => {
            if (!validateForm(form)) {
                e.preventDefault();
            }
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Menu filter functionality
    const setupMenuFilters = () => {
        const filterCheckboxes = document.querySelectorAll('.menu-filters input[type="checkbox"]');
        if (filterCheckboxes.length === 0) return;
        
        // Auto-submit when a filter is changed
        filterCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                checkbox.closest('form').submit();
            });
        });
    };
    
    // Initialize menu filters if present
    setupMenuFilters();

    // Location map functionality
    const setupLocationMap = () => {
        // This would be expanded with actual map integration
        // For example, using the Google Maps API or Mapbox
        const mapContainers = document.querySelectorAll('.map-container, .featured-map');
        if (mapContainers.length === 0) return;
        
        // This is a placeholder for map initialization
        // In a real implementation, you would initialize your map library here
    };
    
    // Initialize location map if present
    setupLocationMap();

    // Bootstrap components initialization
    // This is needed for components that require JavaScript, like accordions
    const initBootstrapComponents = () => {
        // Initialize accordions
        const accordionButtons = document.querySelectorAll('.accordion-button');
        if (accordionButtons.length === 0) return;
        
        accordionButtons.forEach(button => {
            button.addEventListener('click', function() {
                const isExpanded = this.getAttribute('aria-expanded') === 'true';
                this.setAttribute('aria-expanded', !isExpanded);
                
                const target = document.querySelector(this.getAttribute('data-bs-target'));
                if (target) {
                    if (isExpanded) {
                        target.classList.remove('show');
                    } else {
                        target.classList.add('show');
                    }
                }
            });
        });
        
        // Initialize tooltips
        const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltips.forEach(tooltip => {
            tooltip.addEventListener('mouseenter', function() {
                const tooltipContent = document.createElement('div');
                tooltipContent.classList.add('tooltip-inner');
                tooltipContent.textContent = this.getAttribute('data-bs-title');
                
                const tooltipContainer = document.createElement('div');
                tooltipContainer.classList.add('tooltip');
                tooltipContainer.appendChild(tooltipContent);
                
                document.body.appendChild(tooltipContainer);
                
                const rect = this.getBoundingClientRect();
                tooltipContainer.style.position = 'absolute';
                tooltipContainer.style.top = rect.top + window.scrollY - tooltipContainer.offsetHeight - 10 + 'px';
                tooltipContainer.style.left = rect.left + window.scrollX + (rect.width / 2) - (tooltipContainer.offsetWidth / 2) + 'px';
                tooltipContainer.style.opacity = '1';
                
                this.addEventListener('mouseleave', function() {
                    tooltipContainer.remove();
                }, { once: true });
            });
        });
    };
    
    // Initialize Bootstrap components
    initBootstrapComponents();

    // Newsletter form submission
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const emailInput = this.querySelector('input[type="email"]');
            if (!emailInput || !emailInput.value.trim()) return;
            
            // Show a success message
            const successMessage = document.createElement('div');
            successMessage.classList.add('alert', 'alert-success', 'mt-3');
            successMessage.textContent = 'Thank you for subscribing to our newsletter!';
            
            // Clear the input and append the message
            emailInput.value = '';
            this.appendChild(successMessage);
            
            // Remove the message after 5 seconds
            setTimeout(() => {
                successMessage.remove();
            }, 5000);
            
            // In a real implementation, you would send an AJAX request to the server
        });
    }

    // File input customization
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        const fileLabel = input.nextElementSibling;
        if (!fileLabel || !fileLabel.classList.contains('custom-file-label')) return;
        
        input.addEventListener('change', function() {
            if (this.files && this.files.length > 0) {
                fileLabel.textContent = this.files[0].name;
            } else {
                fileLabel.textContent = 'Choose file';
            }
        });
    });

    // Image gallery functionality
    const setupGallery = () => {
        const galleryItems = document.querySelectorAll('.gallery-item img');
        if (galleryItems.length === 0) return;
        
        galleryItems.forEach(item => {
            item.addEventListener('click', function() {
                // Create a lightbox overlay
                const lightbox = document.createElement('div');
                lightbox.classList.add('lightbox');
                lightbox.style.position = 'fixed';
                lightbox.style.top = '0';
                lightbox.style.left = '0';
                lightbox.style.width = '100%';
                lightbox.style.height = '100%';
                lightbox.style.backgroundColor = 'rgba(0, 0, 0, 0.9)';
                lightbox.style.display = 'flex';
                lightbox.style.alignItems = 'center';
                lightbox.style.justifyContent = 'center';
                lightbox.style.zIndex = '9999';
                
                // Create the image
                const img = document.createElement('img');
                img.src = this.src;
                img.style.maxWidth = '90%';
                img.style.maxHeight = '90%';
                img.style.objectFit = 'contain';
                
                // Add a close button
                const closeBtn = document.createElement('button');
                closeBtn.textContent = '×';
                closeBtn.style.position = 'absolute';
                closeBtn.style.top = '20px';
                closeBtn.style.right = '20px';
                closeBtn.style.background = 'none';
                closeBtn.style.border = 'none';
                closeBtn.style.color = '#fff';
                closeBtn.style.fontSize = '40px';
                closeBtn.style.cursor = 'pointer';
                
                // Add to the DOM
                lightbox.appendChild(img);
                lightbox.appendChild(closeBtn);
                document.body.appendChild(lightbox);
                
                // Close on button click or anywhere
                closeBtn.addEventListener('click', () => lightbox.remove());
                lightbox.addEventListener('click', (e) => {
                    if (e.target === lightbox) lightbox.remove();
                });
            });
        });
    };
    
    // Initialize gallery if present
    setupGallery();
});