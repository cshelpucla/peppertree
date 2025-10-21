/**
 * Universal Unit Data Loader
 * Loads unit information from units-data.json and updates page elements
 */

// Load and cache unit data
let unitsData = null;

async function loadUnitsData() {
    if (unitsData) return unitsData;
    
    try {
        const response = await fetch('units-data.json');
        const data = await response.json();
        unitsData = data;
        return data;
    } catch (error) {
        console.error('Error loading units data:', error);
        return null;
    }
}

// Get specific unit by ID
async function getUnitById(unitId) {
    const data = await loadUnitsData();
    if (!data) return null;
    
    return data.units.find(unit => unit.id === unitId.toLowerCase());
}

// Update unit card elements (for index.html and similar pages)
function updateUnitCard(unitCard, unit) {
    if (!unitCard || !unit) return;
    
    // Update unit number/title
    const unitTitleElement = unitCard.querySelector('[data-unit-title]');
    if (unitTitleElement) {
        unitTitleElement.textContent = `Unit ${unit.unitNumber}`;
    }
    
    // Update price
    const priceElement = unitCard.querySelector('[data-price]');
    if (priceElement) {
        priceElement.textContent = `$${unit.price.toLocaleString()}`;
    }
    
    // Update unit type (bedrooms and bathrooms)
    const unitTypeElement = unitCard.querySelector('[data-unit-type]');
    if (unitTypeElement) {
        unitTypeElement.textContent = `${unit.bedrooms} Bedroom • ${unit.bathrooms} Bath Townhome`;
    }
    
    // Update bedroom spec
    const bedroomSpec = unitCard.querySelector('[data-bedrooms]');
    if (bedroomSpec) {
        bedroomSpec.textContent = `🛏️ ${unit.bedrooms} Bed`;
    }
    
    // Update bathroom spec
    const bathroomSpec = unitCard.querySelector('[data-bathrooms]');
    if (bathroomSpec) {
        bathroomSpec.textContent = `🚿 ${unit.bathrooms} Bath`;
    }
    
    // Update description
    const descElement = unitCard.querySelector('[data-description]');
    if (descElement && unit.description && unit.description.length > 0) {
        const fullDesc = unit.description[0];
        const shortDesc = fullDesc.length > 100 ? fullDesc.substring(0, 100) + '...' : fullDesc;
        descElement.textContent = shortDesc;
    }
}

// Update unit detail page (for available-*.html pages)
async function updateUnitDetailPage(unitId) {
    const unit = await getUnitById(unitId);
    if (!unit) {
        console.error(`Unit ${unitId} not found`);
        return;
    }
    
    // Update banner
    const bannerTag = document.querySelector('[data-banner-tag]');
    if (bannerTag) bannerTag.textContent = unit.bannerTag || '🎉 AVAILABLE NOW';
    
    const bannerTitle = document.querySelector('[data-banner-title]');
    if (bannerTitle) bannerTitle.textContent = unit.bannerTitle || `${unit.unitNumber} Available Now!`;
    
    const bannerSubtitle = document.querySelector('[data-banner-subtitle]');
    if (bannerSubtitle) bannerSubtitle.textContent = unit.bannerSubtitle || `${unit.bedrooms} bedroom townhome`;
    
    // Update unit header
    const unitTitle = document.querySelector('[data-unit-header-title]');
    if (unitTitle) unitTitle.textContent = `${unit.unitNumber} - ${unit.bedrooms} Bedroom Townhome`;
    
    const priceAmount = document.querySelector('[data-price-amount]');
    if (priceAmount) priceAmount.textContent = `$${unit.price.toLocaleString()}`;
    
    // Update page title
    const pageTitle = document.querySelector('title');
    if (pageTitle) pageTitle.textContent = `${unit.unitNumber} Available - PepperTree Townhomes`;
    
    // Update detail cards
    const bedroomsDetail = document.querySelector('[data-detail-bedrooms]');
    if (bedroomsDetail) bedroomsDetail.textContent = `${unit.bedrooms} Bedrooms`;
    
    const bedroomsLayout = document.querySelector('[data-detail-bedrooms-layout]');
    if (bedroomsLayout) bedroomsLayout.textContent = unit.layoutDescription || '';
    
    const bathroomsDetail = document.querySelector('[data-detail-bathrooms]');
    if (bathroomsDetail) bathroomsDetail.textContent = `${unit.bathrooms} ${unit.bathrooms > 1 ? 'Full Baths' : 'Bath'}`;
    
    const bathroomsLayout = document.querySelector('[data-detail-bathrooms-layout]');
    if (bathroomsLayout) bathroomsLayout.textContent = unit.bathroomDescription || '';
    
    const unitNumber = document.querySelector('[data-detail-unit-number]');
    if (unitNumber) unitNumber.textContent = unit.unitNumber;
    
    // Update description sections
    const descriptionContainers = document.querySelectorAll('[data-unit-description]');
    if (descriptionContainers.length > 0 && unit.description) {
        descriptionContainers.forEach((container, index) => {
            if (unit.description[index]) {
                container.textContent = unit.description[index];
            }
        });
    }
    
    // Update features list
    const featuresList = document.querySelector('[data-features-list]');
    if (featuresList && unit.interiorFeatures) {
        featuresList.innerHTML = '';
        unit.interiorFeatures.forEach(feature => {
            const li = document.createElement('li');
            li.textContent = feature;
            featuresList.appendChild(li);
        });
    }
    
    // Update photo gallery
    updatePhotoGallery(unit);
}

// Update photo gallery with unit photos
function updatePhotoGallery(unit) {
    if (!unit.photos || unit.photos.length === 0) return;
    
    const mainImage = document.querySelector('#mainImage');
    const photoGrid = document.querySelector('.photo-grid-expanded');
    
    if (mainImage) {
        mainImage.src = `images/${unit.photos[0]}`;
        mainImage.alt = unit.photoDescriptions ? unit.photoDescriptions[0] : unit.unitNumber;
    }
    
    if (photoGrid) {
        photoGrid.innerHTML = '';
        unit.photos.forEach((photo, index) => {
            const img = document.createElement('img');
            img.src = `images/${photo}`;
            img.alt = unit.photoDescriptions && unit.photoDescriptions[index] 
                ? unit.photoDescriptions[index] 
                : `${unit.unitNumber} Photo ${index + 1}`;
            img.className = 'thumbnail-img';
            img.onclick = function() { changeMainImage(this); };
            photoGrid.appendChild(img);
        });
    }
}

// Initialize unit cards on page load (for index.html)
async function initializeUnitCards() {
    const data = await loadUnitsData();
    if (!data) return;
    
    data.units.forEach(unit => {
        const unitCard = document.querySelector(`[data-unit-id="${unit.id}"]`);
        if (unitCard) {
            updateUnitCard(unitCard, unit);
        }
    });
}

// Auto-detect unit ID from URL parameter or page
function getUnitIdFromPage() {
    // Check URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const unitParam = urlParams.get('unit');
    if (unitParam) return unitParam;
    
    // Check if page filename contains unit ID
    const pathname = window.location.pathname;
    const match = pathname.match(/available-(720c|161d|151a)/i);
    if (match) return match[1];
    
    return null;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', async function() {
    // Check if this is a unit detail page
    const unitId = getUnitIdFromPage();
    if (unitId) {
        await updateUnitDetailPage(unitId);
    } else {
        // Initialize unit cards for listing pages
        await initializeUnitCards();
    }
});
