# Adding Real Images to PepperTree Townhomes Website

## Quick Guide to Replace Placeholder Images

The website currently uses colorful gradient placeholders with emoji icons. Here's how to add real photos:

---

## 📸 Recommended Images to Add

### 1. **Neighborhood Attractions** (neighborhood.html)

Replace the gradient backgrounds in the `.highlight-image` sections:

#### R.C. Baker Memorial Museum
- **Current**: `background: linear-gradient(135deg, #8B4513 0%, #D2691E 100%);`
- **Replace with**: `background-image: url('images/museum.jpg');`
- **Photo suggestions**: Museum exterior, vintage gas station, artifacts display

#### Horned Toad Derby
- **Current**: `background: linear-gradient(135deg, #228B22 0%, #90EE90 100%);`
- **Replace with**: `background-image: url('images/toad-derby.jpg');`
- **Photo suggestions**: Derby event, horned lizards, crowd enjoying the event

#### WHAMOBASS Balloon Rally
- **Current**: `background: linear-gradient(135deg, #FF6B6B 0%, #FFE66D 100%);`
- **Replace with**: `background-image: url('images/balloon-rally.jpg');`
- **Photo suggestions**: Hot air balloons at dawn, balloon ascension, colorful balloons

#### Harris Ranch Resort
- **Current**: `background: linear-gradient(135deg, #8B4513 0%, #CD853F 100%);`
- **Replace with**: `background-image: url('images/harris-ranch.jpg');`
- **Photo suggestions**: Restaurant exterior, resort grounds, steakhouse interior

#### West Hills College
- **Current**: `background: linear-gradient(135deg, #4A90E2 0%, #87CEEB 100%);`
- **Replace with**: `background-image: url('images/college.jpg');`
- **Photo suggestions**: Campus buildings, athletic facilities, students

#### Pleasant Valley
- **Current**: `background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);`
- **Replace with**: `background-image: url('images/valley.jpg');`
- **Photo suggestions**: Valley landscape, surrounding hills, sunset views

---

### 2. **Gallery Page** (gallery.html)

Replace all gradient backgrounds in `.gallery-item` sections:

**Sections to update:**
- Community Exterior
- Living Room
- Kitchen  
- Bedroom
- Pool Area
- Fitness Center
- Landscaping
- Bathroom
- Dining Area
- Clubhouse
- Parking Area
- Community View

---

### 3. **Floor Plans** (floorplans.html)

Replace in `.floorplan-image` sections:
- 2 BR floorplan diagram
- 3 BR floorplan diagram

---

## 🔧 How to Add Images

### Step 1: Create Images Folder
```
PepperTree/
├── images/
│   ├── museum.jpg
│   ├── toad-derby.jpg
│   ├── balloon-rally.jpg
│   ├── harris-ranch.jpg
│   ├── college.jpg
│   ├── valley.jpg
│   ├── exterior.jpg
│   ├── kitchen.jpg
│   └── ... (other images)
```

### Step 2: Replace in HTML Files

**Example - neighborhood.html:**

**BEFORE:**
```html
<div class="highlight-image" style="background: linear-gradient(135deg, #8B4513 0%, #D2691E 100%);">
    <div class="image-placeholder">🏛️</div>
</div>
```

**AFTER:**
```html
<div class="highlight-image" style="background-image: url('images/museum.jpg'); background-size: cover; background-position: center;">
    <!-- Remove or hide the emoji placeholder -->
</div>
```

### Step 3: Update Gallery Images

**BEFORE:**
```html
<div class="gallery-item" data-category="exterior" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
    <div class="gallery-placeholder">Community Exterior</div>
    <div class="gallery-overlay">
        <h4>Community Entrance</h4>
        <p>Welcoming exterior view</p>
    </div>
</div>
```

**AFTER:**
```html
<div class="gallery-item" data-category="exterior" style="background-image: url('images/exterior-1.jpg'); background-size: cover; background-position: center;">
    <div class="gallery-overlay">
        <h4>Community Entrance</h4>
        <p>Welcoming exterior view</p>
    </div>
</div>
```

---

## 📷 Where to Get Images

### Option 1: Free Stock Photos
- **Unsplash**: https://unsplash.com/
- **Pexels**: https://pexels.com/
- **Pixabay**: https://pixabay.com/

**Search terms:**
- "apartment exterior"
- "modern kitchen"
- "living room interior"
- "swimming pool amenity"
- "fitness center"
- "California landscape"
- "hot air balloons"

### Option 2: Local Sources
- Coalinga Chamber of Commerce
- West Hills College Coalinga website
- Harris Ranch website (with permission)
- City of Coalinga tourism photos
- R.C. Baker Memorial Museum

### Option 3: Take Your Own
- Visit PepperTree Townhomes location
- Photograph local attractions
- Capture community features
- Get permission for private properties

---

## 🎨 Image Specifications

### Recommended Sizes:
- **Gallery items**: 800x600px or larger
- **Highlight cards**: 640x400px or larger  
- **Floor plans**: 1200x900px (for detail)
- **Hero section**: 1920x1080px (full width)

### Format:
- **Primary**: JPG (smaller file size)
- **Alternative**: WebP (modern, efficient)
- **Graphics**: PNG (logos, icons)

### Optimization:
- Compress images before uploading
- Use tools like TinyPNG or ImageOptim
- Target file size: under 200KB per image

---

## 🔄 Quick CSS Updates for Images

Add this to `styles.css` for better image display:

```css
.highlight-image[style*="background-image"] .image-placeholder {
    display: none; /* Hide emoji when real image is used */
}

.gallery-item[style*="background-image"] .gallery-placeholder {
    display: none; /* Hide placeholder text when real image is used */
}

/* Ensure images cover properly */
.highlight-image,
.gallery-item {
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
```

---

## ✅ Testing Checklist

After adding images:
- [ ] Images load on all pages
- [ ] Images are properly sized
- [ ] Mobile responsive works
- [ ] File sizes are optimized
- [ ] All links work correctly
- [ ] Gallery filters still function
- [ ] Hover effects still work

---

## 📝 Notes

1. **Copyright**: Ensure you have rights to use all images
2. **Optimization**: Compress images to maintain site performance
3. **Alt Text**: Add descriptive alt text for accessibility
4. **Backup**: Keep original high-res versions separate
5. **Consistency**: Maintain similar style/quality across images

---

## Example: Full Image Implementation

```html
<!-- In neighborhood.html, replace highlight card -->
<div class="highlight-card-visual">
    <div class="highlight-image" style="background-image: url('images/harris-ranch.jpg'); background-size: cover; background-position: center;">
    </div>
    <div class="highlight-content">
        <h4>Harris Ranch Resort</h4>
        <p>Famous cattle ranch just 13 miles northeast on I-5...</p>
        <a href="https://www.harrisranch.com" target="_blank" class="learn-more">Visit Website →</a>
    </div>
</div>
```

---

For questions or assistance with image implementation, refer to the main README.md file.
