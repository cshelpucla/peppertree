/**
 * Photo Carousel and Lightbox System for Unit Cards
 */

// Carousel state management
const carousels = new Map();
let lightboxImages = [];
let currentLightboxIndex = 0;

/**
 * Initialize carousels for all units on the page
 */
async function initCarousels() {
    try {
        // Fetch units data
        const response = await fetch('units-data.json');
        if (!response.ok) throw new Error('Failed to load units data');
        const data = await response.json();
        
        // Initialize each unit carousel
        data.units.forEach(unit => {
            const track = document.querySelector(`[data-carousel="${unit.id}"]`);
            if (!track) return;
            
            // Create carousel state
            carousels.set(unit.id, {
                currentIndex: 0,
                images: unit.photos || [],
                descriptions: unit.photoDescriptions || [],
                autoPlayInterval: null
            });
            
            // Load images into carousel
            loadCarouselImages(unit.id, unit.photos, unit.photoDescriptions, unit.unitNumber);
            
            // Setup navigation
            setupCarouselNavigation(unit.id);
            
            // Start auto-rotation
            startAutoRotation(unit.id);
        });
        
    } catch (error) {
        console.error('Error initializing carousels:', error);
    }
}

/**
 * Load images into a carousel
 */
function loadCarouselImages(unitId, photos, descriptions, unitNumber) {
    const track = document.querySelector(`[data-carousel="${unitId}"]`);
    const dotsContainer = document.querySelector(`[data-carousel-dots="${unitId}"]`);
    
    if (!track || !photos || photos.length === 0) return;
    
    // Clear existing content
    track.innerHTML = '';
    dotsContainer.innerHTML = '';
    
    // Add images
    photos.forEach((photo, index) => {
        const img = document.createElement('img');
        img.src = `images/${photo}`;
        img.alt = descriptions[index] || `${unitNumber} - Photo ${index + 1}`;
        img.className = index === 0 ? 'active' : '';
        img.dataset.index = index;
        img.dataset.unitId = unitId;
        
        // Click to open lightbox
        img.addEventListener('click', (e) => {
            e.stopPropagation();
            openLightbox(unitId, index);
        });
        
        track.appendChild(img);
        
        // Add dot indicator
        const dot = document.createElement('button');
        dot.className = `carousel-dot ${index === 0 ? 'active' : ''}`;
        dot.dataset.index = index;
        dot.addEventListener('click', (e) => {
            e.stopPropagation();
            goToSlide(unitId, index);
        });
        dotsContainer.appendChild(dot);
    });
}

/**
 * Setup carousel navigation buttons
 */
function setupCarouselNavigation(unitId) {
    const prevBtn = document.querySelector(`[data-carousel-prev="${unitId}"]`);
    const nextBtn = document.querySelector(`[data-carousel-next="${unitId}"]`);
    const container = document.querySelector(`[data-carousel="${unitId}"]`).closest('.carousel-container');
    
    if (prevBtn) {
        prevBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            e.preventDefault();
            previousSlide(unitId);
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            e.preventDefault();
            nextSlide(unitId);
        });
    }
    
    // Pause auto-rotation on hover
    if (container) {
        container.addEventListener('mouseenter', () => pauseAutoRotation(unitId));
        container.addEventListener('mouseleave', () => startAutoRotation(unitId));
    }
}

/**
 * Go to specific slide
 */
function goToSlide(unitId, index) {
    const carousel = carousels.get(unitId);
    if (!carousel) return;
    
    const track = document.querySelector(`[data-carousel="${unitId}"]`);
    const images = track.querySelectorAll('img');
    const dots = document.querySelectorAll(`[data-carousel-dots="${unitId}"] .carousel-dot`);
    
    // Remove active class from all
    images.forEach(img => img.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));
    
    // Add active class to current
    if (images[index]) images[index].classList.add('active');
    if (dots[index]) dots[index].classList.add('active');
    
    carousel.currentIndex = index;
}

/**
 * Go to next slide
 */
function nextSlide(unitId) {
    const carousel = carousels.get(unitId);
    if (!carousel) return;
    
    const nextIndex = (carousel.currentIndex + 1) % carousel.images.length;
    goToSlide(unitId, nextIndex);
}

/**
 * Go to previous slide
 */
function previousSlide(unitId) {
    const carousel = carousels.get(unitId);
    if (!carousel) return;
    
    const prevIndex = carousel.currentIndex === 0 
        ? carousel.images.length - 1 
        : carousel.currentIndex - 1;
    goToSlide(unitId, prevIndex);
}

/**
 * Start automatic rotation
 */
function startAutoRotation(unitId) {
    const carousel = carousels.get(unitId);
    if (!carousel) return;
    
    // Clear existing interval
    if (carousel.autoPlayInterval) {
        clearInterval(carousel.autoPlayInterval);
    }
    
    // Start new interval (rotate every 4 seconds)
    carousel.autoPlayInterval = setInterval(() => {
        nextSlide(unitId);
    }, 4000);
}

/**
 * Pause automatic rotation
 */
function pauseAutoRotation(unitId) {
    const carousel = carousels.get(unitId);
    if (!carousel) return;
    
    if (carousel.autoPlayInterval) {
        clearInterval(carousel.autoPlayInterval);
        carousel.autoPlayInterval = null;
    }
}

/**
 * Open lightbox with image
 */
function openLightbox(unitId, startIndex) {
    const carousel = carousels.get(unitId);
    if (!carousel) return;
    
    // Set lightbox images
    lightboxImages = carousel.images.map((photo, index) => ({
        src: `images/${photo}`,
        caption: carousel.descriptions[index] || `Photo ${index + 1}`
    }));
    
    currentLightboxIndex = startIndex;
    
    // Show lightbox
    const lightbox = document.getElementById('imageLightbox');
    const lightboxImg = document.getElementById('lightboxImage');
    const lightboxCaption = document.getElementById('lightboxCaption');
    
    if (lightbox && lightboxImg && lightboxCaption) {
        lightboxImg.src = lightboxImages[currentLightboxIndex].src;
        lightboxCaption.textContent = lightboxImages[currentLightboxIndex].caption;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

/**
 * Close lightbox
 */
function closeLightbox() {
    const lightbox = document.getElementById('imageLightbox');
    if (lightbox) {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }
}

/**
 * Show next image in lightbox
 */
function nextLightboxImage() {
    currentLightboxIndex = (currentLightboxIndex + 1) % lightboxImages.length;
    updateLightboxImage();
}

/**
 * Show previous image in lightbox
 */
function previousLightboxImage() {
    currentLightboxIndex = currentLightboxIndex === 0 
        ? lightboxImages.length - 1 
        : currentLightboxIndex - 1;
    updateLightboxImage();
}

/**
 * Update lightbox image
 */
function updateLightboxImage() {
    const lightboxImg = document.getElementById('lightboxImage');
    const lightboxCaption = document.getElementById('lightboxCaption');
    
    if (lightboxImg && lightboxCaption && lightboxImages[currentLightboxIndex]) {
        lightboxImg.src = lightboxImages[currentLightboxIndex].src;
        lightboxCaption.textContent = lightboxImages[currentLightboxIndex].caption;
    }
}

/**
 * Initialize lightbox controls
 */
function initLightbox() {
    const lightbox = document.getElementById('imageLightbox');
    const closeBtn = lightbox?.querySelector('.lightbox-close');
    const prevBtn = lightbox?.querySelector('.lightbox-prev');
    const nextBtn = lightbox?.querySelector('.lightbox-next');
    
    if (closeBtn) {
        closeBtn.addEventListener('click', closeLightbox);
    }
    
    if (prevBtn) {
        prevBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            previousLightboxImage();
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            nextLightboxImage();
        });
    }
    
    // Close on background click
    if (lightbox) {
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });
    }
    
    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        const lightbox = document.getElementById('imageLightbox');
        if (!lightbox?.classList.contains('active')) return;
        
        switch(e.key) {
            case 'Escape':
                closeLightbox();
                break;
            case 'ArrowLeft':
                previousLightboxImage();
                break;
            case 'ArrowRight':
                nextLightboxImage();
                break;
        }
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initCarousels();
    initLightbox();
});
