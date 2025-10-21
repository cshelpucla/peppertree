// Unit Data Loader
(function() {
    // Get unit ID from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const unitId = urlParams.get('unit');
    
    if (!unitId) {
        console.error('No unit ID specified in URL');
        return;
    }

    // Load units data
    fetch('units-data.json')
        .then(response => response.json())
        .then(data => {
            // Find the specific unit
            const unit = data.units.find(u => u.id === unitId);
            
            if (!unit) {
                console.error('Unit not found:', unitId);
                return;
            }
            
            // Populate the page with unit data
            populateUnitData(unit, data);
            
            // Load other units for cross-promotion
            loadOtherUnits(data.units, unitId);
        })
        .catch(error => {
            console.error('Error loading unit data:', error);
        });

    function populateUnitData(unit, data) {
        // Banner section
        document.getElementById('bannerTag').textContent = unit.bannerTag;
        document.getElementById('bannerTitle').textContent = unit.bannerTitle;
        document.getElementById('bannerSubtitle').textContent = unit.bannerSubtitle;
        
        // Unit header
        document.getElementById('unitTitle').textContent = unit.title;
        document.getElementById('unitPrice').textContent = '$' + unit.price;
        
        // Unit details
        document.getElementById('unitNumber').textContent = unit.unitNumber;
        document.getElementById('bedroomCount').textContent = unit.bedrooms;
        document.getElementById('layoutDesc').textContent = unit.layoutDescription;
        document.getElementById('bathroomCount').textContent = unit.bathrooms;
        document.getElementById('bathroomDesc').textContent = unit.bathroomDescription;
        document.getElementById('priceDisplay').textContent = '$' + unit.price;
        document.getElementById('specialTag').textContent = unit.specialTag;
        
        // Description section
        document.getElementById('unitNumberDesc').textContent = unit.unitNumber;
        const descContent = document.getElementById('descriptionContent');
        descContent.innerHTML = '';
        unit.description.forEach(paragraph => {
            const p = document.createElement('p');
            p.textContent = paragraph;
            descContent.appendChild(p);
        });
        
        // Photo gallery
        if (unit.photos && unit.photos.length > 0) {
            const mainImage = document.getElementById('mainImage');
            mainImage.src = 'images/' + unit.photos[0];
            mainImage.alt = unit.photoDescriptions[0];
            
            const photoGrid = document.getElementById('photoGrid');
            photoGrid.innerHTML = '';
            
            unit.photos.forEach((photo, index) => {
                const img = document.createElement('img');
                img.src = 'images/' + photo;
                img.alt = unit.photoDescriptions[index];
                img.className = 'thumbnail-img';
                img.onclick = function() { changeMainImage(this); };
                photoGrid.appendChild(img);
            });
        }
        
        // Interior features
        const interiorList = document.getElementById('interiorFeaturesList');
        interiorList.innerHTML = '';
        unit.interiorFeatures.forEach(feature => {
            const li = document.createElement('li');
            li.textContent = '✓ ' + feature;
            interiorList.appendChild(li);
        });
        
        // Community amenities
        const amenitiesList = document.getElementById('communityAmenitiesList');
        amenitiesList.innerHTML = '';
        data.communityAmenities.forEach(amenity => {
            const li = document.createElement('li');
            li.textContent = '✓ ' + amenity;
            amenitiesList.appendChild(li);
        });
        
        // Location features
        const locationList = document.getElementById('locationFeaturesList');
        locationList.innerHTML = '';
        data.locationFeatures.forEach(feature => {
            const li = document.createElement('li');
            li.textContent = '✓ ' + feature;
            locationList.appendChild(li);
        });
        
        // Lease information
        document.getElementById('leasePrice').textContent = '$' + unit.price;
        document.getElementById('securityDeposit').textContent = data.leaseInfo.securityDeposit;
        document.getElementById('leaseTerm').textContent = data.leaseInfo.leaseTerm;
        document.getElementById('availability').textContent = data.leaseInfo.availability;
        document.getElementById('leaseUnitNumber').textContent = unit.unitNumber;
        
        // CTA section
        document.getElementById('ctaUnitNumber').textContent = unit.unitNumber;
        document.getElementById('ctaMessage').textContent = 
            `This ${unit.bedrooms}-bedroom townhome is ready for you! Contact us today to schedule a tour.`;
        
        // Update page title
        document.title = unit.title + ' - PepperTree Townhomes';
    }

    function loadOtherUnits(allUnits, currentUnitId) {
        const otherUnits = allUnits.filter(u => u.id !== currentUnitId);
        const otherUnitsGrid = document.getElementById('otherUnitsGrid');
        otherUnitsGrid.innerHTML = '';
        
        otherUnits.forEach(unit => {
            const card = document.createElement('div');
            card.className = 'plan-card';
            
            card.innerHTML = `
                <h3>${unit.unitNumber}</h3>
                <p class="plan-specs">${unit.bedrooms} Bed • ${unit.bathrooms} Bath</p>
                <p class="plan-price">$${unit.price}/month</p>
                <a href="unit-template.html?unit=${unit.id}" class="btn btn-outline" style="margin-top: 15px;">View Details</a>
            `;
            
            otherUnitsGrid.appendChild(card);
        });
    }
})();
