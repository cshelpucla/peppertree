# PepperTree Townhomes Website

A modern, responsive website for PepperTree Townhomes apartment complex.

## Features

- **Multi-Page Structure**: Separate pages for each major section
- **Responsive Design**: Works beautifully on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design inspired by contemporary apartment websites
- **Interactive Elements**: Smooth scrolling, animations, and interactive navigation
- **Floor Plans Page**: Dedicated page showcasing both 2-bedroom and 3-bedroom townhomes with 1.5 baths
- **Amenities Page**: Comprehensive list of community and apartment features
- **Photo Gallery**: Interactive gallery with category filters (Exterior, Interior, Amenities)
- **Contact Form**: Detailed inquiry form with multiple contact options and FAQ
- **Neighborhood Page**: Extensive information about location and nearby services

## File Structure

```
PepperTree/
├── index.html         # Home page
├── floorplans.html    # Floor plans page
├── amenities.html     # Amenities page
├── gallery.html       # Photo gallery page
├── neighborhood.html  # Neighborhood information page
├── contact.html       # Contact and inquiry form page
├── styles.css         # All styling and responsive design
├── script.js          # Interactive functionality
└── README.md          # This file
```

## How to View

### Option 1: Direct File Opening
Simply open `index.html` in any modern web browser (Chrome, Firefox, Edge, Safari)

### Option 2: Local Server (Recommended)
For the best experience, serve the files using a local web server:

**Using Python:**
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

**Using Node.js (http-server):**
```bash
npx http-server -p 8000
```

**Using PHP:**
```bash
php -S localhost:8000
```

Then open your browser to: `http://localhost:8000`

## Customization Guide

### Update Property Information

1. **Contact Details** (in `index.html`):
   - Search for "Contact Us" section
   - Update address, phone number, and email

2. **Office Hours**:
   - Located in the contact section
   - Modify times as needed

3. **Colors** (in `styles.css`):
   ```css
   :root {
       --primary-color: #2c5f2d;    /* Main green color */
       --secondary-color: #97be5a;   /* Accent green */
       --accent-color: #ffc857;      /* Yellow accent */
   }
   ```

4. **Floor Plan Details**:
   - Update square footage, features, and pricing in the floor plans section

5. **Amenities**:
   - Add or remove amenity cards in the amenities section

### Adding Real Images

Replace the placeholder gradients with real images:

1. Create an `images` folder in the same directory
2. Add your photos (e.g., `exterior.jpg`, `kitchen.jpg`, etc.)
3. In `index.html`, update the gallery items:
   ```html
   <div class="gallery-item" style="background-image: url('images/exterior.jpg');">
   ```

4. For the hero section, add a background image:
   ```css
   .hero {
       background-image: url('images/hero-background.jpg');
   }
   ```

## Pages Overview

### 1. Home Page (index.html)
- **Hero Section**: Eye-catching banner with call-to-action buttons
- **Introduction**: Welcome text and quick navigation cards
- **Preview Sections**: Highlights from floor plans, amenities, gallery, and neighborhood
- **Contact Section**: Quick contact form
- **Footer**: Links, social media, and legal information

### 2. Floor Plans Page (floorplans.html)
- Detailed 2BR and 3BR townhome information
- Specifications (bedrooms, bathrooms, square footage)
- Feature lists for each floor plan
- "Why Choose PepperTree" section
- Direct links to contact and amenities

### 3. Amenities Page (amenities.html)
- Community amenities grid (12+ amenities)
- Apartment features section
- Detailed feature lists organized by category
- Links to gallery and contact

### 4. Gallery Page (gallery.html)
- Interactive photo gallery with 12+ placeholder images
- Filter buttons (All, Exterior, Interior, Amenities)
- Hover overlays with descriptions
- Call-to-action to schedule tours

### 5. Neighborhood Page (neighborhood.html)
- Location overview
- "What's Nearby" section with 6 categories
- Transportation and commuting information
- Map placeholder for future integration

### 6. Contact Page (contact.html)
- Comprehensive contact information
- Office hours
- Emergency maintenance contact
- Detailed inquiry form
- FAQ section
- Application information

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Future Enhancements

- Integrate with a backend for form submissions
- Add real photo gallery with lightbox
- Integrate Google Maps for location
- Add virtual tour functionality
- Connect to apartment management software for real-time availability
- Add online application portal
- Implement resident portal login

## Notes

- The contact form currently shows an alert message. In production, you'll need to integrate with a backend service or email API
- Gallery images are placeholders with gradients - replace with actual property photos
- The map is a placeholder - integrate Google Maps API for interactive map
- Update all placeholder text with actual property information

## Technologies Used

- HTML5
- CSS3 (with CSS Grid and Flexbox)
- Vanilla JavaScript (no dependencies)
- Google Fonts (Montserrat & Playfair Display)

## License

© 2025 PepperTree Townhomes. All rights reserved.
