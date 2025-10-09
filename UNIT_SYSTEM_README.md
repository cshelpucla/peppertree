# PepperTree Townhomes - Dynamic Unit System

## Overview
The website now uses a dynamic template system for displaying available units. All unit information is stored in a central JSON file (`units-data.json`), making it easy to update content without editing HTML files.

## File Structure

### Core Files
- **`units-data.json`** - Central database for all unit information
- **`unit-template.html`** - Dynamic template page for displaying units
- **`unit-loader.js`** - JavaScript that loads and renders unit data

### Legacy Files (can be removed)
- `available-720c.html`
- `available-730a.html`
- `available-151a.html`

## How It Works

### Accessing Unit Pages
Units are accessed via URL parameters:
- Unit 720C: `unit-template.html?unit=720c`
- Unit 730A: `unit-template.html?unit=730a`
- Unit 151A: `unit-template.html?unit=151a`

### JSON Data Structure

```json
{
  "units": [
    {
      "id": "720c",                    // Unique identifier (used in URL)
      "unitNumber": "720C",             // Display number
      "title": "Unit 720C - ...",       // Page title
      "bedrooms": 3,                    // Number of bedrooms
      "bathrooms": 2,                   // Number of bathrooms
      "price": 1195,                    // Monthly rent
      "featured": true,                 // Show as featured
      "status": "available",            // Availability status
      "bannerTag": "🎉 MOVE-IN READY",  // Banner label
      "bannerTitle": "...",             // Banner heading
      "bannerSubtitle": "...",          // Banner description
      "layoutDescription": "...",       // Bedroom layout
      "bathroomDescription": "...",     // Bathroom details
      "specialTag": "...",              // Special offer text
      "description": [                  // Array of paragraphs
        "First paragraph...",
        "Second paragraph..."
      ],
      "photos": [                       // Array of image filenames
        "720C_LivingRoom.jpg",
        "720C_Kitchen.jpg"
      ],
      "photoDescriptions": [            // Alt text for photos
        "Living Room",
        "Kitchen"
      ],
      "interiorFeatures": [             // List of features
        "Feature 1",
        "Feature 2"
      ]
    }
  ],
  "communityAmenities": [],             // Shared amenities
  "locationFeatures": [],               // Shared location features
  "leaseInfo": {                        // Shared lease terms
    "securityDeposit": "...",
    "leaseTerm": "...",
    "availability": "...",
    "pets": "..."
  }
}
```

## Updating Unit Information

### To Add a New Unit:
1. Open `units-data.json`
2. Add a new unit object to the `units` array
3. Ensure all required fields are filled
4. Add photos to the `images/` directory
5. Unit will automatically appear on the homepage

### To Update Existing Unit:
1. Open `units-data.json`
2. Find the unit by its `id`
3. Modify any fields (price, description, photos, etc.)
4. Save the file - changes are immediate

### To Update Shared Information:
- **Community Amenities**: Edit the `communityAmenities` array
- **Location Features**: Edit the `locationFeatures` array
- **Lease Terms**: Edit the `leaseInfo` object

## Benefits of This System

1. **Centralized Management**: All unit data in one file
2. **Easy Updates**: Change prices, descriptions, or photos without touching HTML
3. **Consistency**: All units use the same template
4. **Scalability**: Easy to add new units
5. **Maintainability**: Reduce code duplication

## Photo Management

Photos must be:
- Placed in the `images/` directory
- Referenced by filename in the JSON file
- Listed in the same order as `photoDescriptions`

Example:
```json
"photos": ["unit1.jpg", "unit2.jpg"],
"photoDescriptions": ["Living Room", "Kitchen"]
```

## Homepage Integration

The homepage (`index.html`) links to units using:
```html
<a href="unit-template.html?unit=720c">View Details</a>
```

The `unit` parameter matches the `id` in the JSON file.

## Browser Compatibility

This system requires:
- Modern browser with JavaScript enabled
- Support for `fetch()` API
- Support for ES6 features (arrow functions, template literals)

All modern browsers (Chrome, Firefox, Safari, Edge) are supported.

## Testing

To test locally:
1. Start the Python HTTP server: `python -m http.server 8000`
2. Navigate to: `http://localhost:8000/unit-template.html?unit=720c`
3. Verify all data loads correctly
4. Test other unit IDs (730a, 151a)

## Future Enhancements

Potential improvements:
- Add unit comparison feature
- Implement availability calendar
- Add virtual tour integration
- Create admin interface for JSON editing
- Add unit filtering/sorting
