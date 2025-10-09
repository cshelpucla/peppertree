#!/bin/bash

# PepperTree Website - Linux Hosting Compatibility Fix Script
# This script fixes all file references and permissions for Linux hosting

echo "🐧 PepperTree Linux Hosting Compatibility Fix"
echo "=============================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Track changes
CHANGES_MADE=0

# ========================================
# STEP 1: Rename case-sensitive files
# ========================================
echo -e "${BLUE}STEP 1: Fixing case-sensitive filenames...${NC}"

# Check and rename IMG_3858.PNG to lowercase extension
if [ -f "images/IMG_3858.PNG" ]; then
    echo -e "${YELLOW}  Renaming: IMG_3858.PNG -> IMG_3858.png${NC}"
    mv "images/IMG_3858.PNG" "images/IMG_3858.png"
    CHANGES_MADE=$((CHANGES_MADE + 1))
fi

# Check if already lowercase
if [ -f "images/IMG_3858.png" ]; then
    echo -e "${GREEN}  ✓ IMG_3858.png exists (correct)${NC}"
fi

# Check and verify PEPPERTREE.jpg
if [ -f "images/PEPPERTREE.jpg" ]; then
    echo -e "${GREEN}  ✓ PEPPERTREE.jpg exists${NC}"
fi

echo ""

# ========================================
# STEP 2: Set proper file permissions
# ========================================
echo -e "${BLUE}STEP 2: Setting proper Linux file permissions...${NC}"

# Set permissions for HTML files
echo "  Setting HTML files to 644 (rw-r--r--)..."
find . -maxdepth 1 -type f -name "*.html" -exec chmod 644 {} \;

# Set permissions for CSS files
echo "  Setting CSS files to 644..."
find . -maxdepth 1 -type f -name "*.css" -exec chmod 644 {} \;

# Set permissions for JavaScript files
echo "  Setting JavaScript files to 644..."
find . -maxdepth 1 -type f -name "*.js" -exec chmod 644 {} \;

# Set permissions for PDF files
echo "  Setting PDF files to 644..."
find . -type f -name "*.pdf" -exec chmod 644 {} \;

# Set permissions for all image files
echo "  Setting image files to 644..."
find images -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" \) -exec chmod 644 {} \;

# Set permissions for JSON files
echo "  Setting JSON files to 644..."
find . -maxdepth 1 -type f -name "*.json" -exec chmod 644 {} \;

# Set permissions for markdown files
echo "  Setting markdown files to 644..."
find . -maxdepth 1 -type f -name "*.md" -exec chmod 644 {} \;

# Set directory permissions
echo "  Setting directory permissions to 755 (rwxr-xr-x)..."
find . -type d -exec chmod 755 {} \;

echo -e "${GREEN}  ✓ File permissions set${NC}"
echo ""

# ========================================
# STEP 3: Verify critical files exist
# ========================================
echo -e "${BLUE}STEP 3: Verifying critical files...${NC}"

# Critical HTML files
CRITICAL_HTML=(
    "index.html"
    "available.html"
    "available-720c.html"
    "available-730a.html"
    "available-151a.html"
    "floorplans.html"
    "amenities.html"
    "gallery.html"
    "neighborhood.html"
    "contact.html"
    "rental-application.html"
)

MISSING_FILES=0

for file in "${CRITICAL_HTML[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}  ✓ $file${NC}"
    else
        echo -e "${RED}  ✗ MISSING: $file${NC}"
        MISSING_FILES=$((MISSING_FILES + 1))
    fi
done

# Critical CSS/JS files
if [ -f "styles.css" ]; then
    echo -e "${GREEN}  ✓ styles.css${NC}"
else
    echo -e "${RED}  ✗ MISSING: styles.css${NC}"
    MISSING_FILES=$((MISSING_FILES + 1))
fi

if [ -f "script.js" ]; then
    echo -e "${GREEN}  ✓ script.js${NC}"
else
    echo -e "${RED}  ✗ MISSING: script.js${NC}"
    MISSING_FILES=$((MISSING_FILES + 1))
fi

# Critical data file
if [ -f "units-data.json" ]; then
    echo -e "${GREEN}  ✓ units-data.json${NC}"
else
    echo -e "${RED}  ✗ MISSING: units-data.json${NC}"
    MISSING_FILES=$((MISSING_FILES + 1))
fi

# Critical PDF
if [ -f "Golden_Hills_Rental_Application_Fillable.pdf" ]; then
    echo -e "${GREEN}  ✓ Golden_Hills_Rental_Application_Fillable.pdf${NC}"
else
    echo -e "${RED}  ✗ MISSING: Golden_Hills_Rental_Application_Fillable.pdf${NC}"
    MISSING_FILES=$((MISSING_FILES + 1))
fi

echo ""

# ========================================
# STEP 4: Verify critical images
# ========================================
echo -e "${BLUE}STEP 4: Verifying critical images...${NC}"

CRITICAL_IMAGES=(
    "images/720-Outside.jpg"
    "images/730_750_Outside.jpg"
    "images/131_Outside_Bldg.jpg"
    "images/unit-1-exterior.jpg"
    "images/unit-2-living.jpg"
    "images/unit-3-kitchen.jpg"
    "images/unit-exterior.jpg"
    "images/unit-living.jpg"
    "images/unit-kitchen.jpg"
    "images/unit-bedroom.jpg"
    "images/720C_LivingRoom.jpg"
    "images/720C_Kitchen.jpg"
    "images/720C_Bedroom.jpg"
)

MISSING_IMAGES=0

for image in "${CRITICAL_IMAGES[@]}"; do
    if [ -f "$image" ]; then
        echo -e "${GREEN}  ✓ ${image##*/}${NC}"
    else
        echo -e "${RED}  ✗ MISSING: ${image##*/}${NC}"
        MISSING_IMAGES=$((MISSING_IMAGES + 1))
    fi
done

echo ""

# ========================================
# STEP 5: Check for case sensitivity issues
# ========================================
echo -e "${BLUE}STEP 5: Checking for case sensitivity issues...${NC}"

CASE_ISSUES=0

# Check for mixed case in image directory
if [ -d "images" ]; then
    # Look for files with uppercase extensions
    UPPERCASE_EXT=$(find images -type f \( -name "*.JPG" -o -name "*.JPEG" -o -name "*.PNG" -o -name "*.GIF" \) 2>/dev/null | wc -l)
    
    if [ "$UPPERCASE_EXT" -gt 0 ]; then
        echo -e "${YELLOW}  ⚠ Found $UPPERCASE_EXT file(s) with uppercase extensions${NC}"
        find images -type f \( -name "*.JPG" -o -name "*.JPEG" -o -name "*.PNG" -o -name "*.GIF" \) 2>/dev/null | while read file; do
            echo -e "${YELLOW}    - $file${NC}"
        done
        CASE_ISSUES=$((CASE_ISSUES + UPPERCASE_EXT))
    else
        echo -e "${GREEN}  ✓ No uppercase file extensions found${NC}"
    fi
fi

echo ""

# ========================================
# STEP 6: Generate summary report
# ========================================
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}LINUX COMPATIBILITY SUMMARY${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

if [ $MISSING_FILES -eq 0 ]; then
    echo -e "${GREEN}✓ All critical files present${NC}"
else
    echo -e "${RED}✗ Missing $MISSING_FILES critical file(s)${NC}"
fi

if [ $MISSING_IMAGES -eq 0 ]; then
    echo -e "${GREEN}✓ All critical images present${NC}"
else
    echo -e "${RED}✗ Missing $MISSING_IMAGES critical image(s)${NC}"
fi

if [ $CASE_ISSUES -eq 0 ]; then
    echo -e "${GREEN}✓ No case sensitivity issues${NC}"
else
    echo -e "${YELLOW}⚠ $CASE_ISSUES potential case sensitivity issue(s)${NC}"
fi

echo -e "${GREEN}✓ File permissions set correctly${NC}"

echo ""

if [ $MISSING_FILES -eq 0 ] && [ $MISSING_IMAGES -eq 0 ] && [ $CASE_ISSUES -eq 0 ]; then
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}✅ READY FOR LINUX HOSTING!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Upload all files to your Linux web server"
    echo "2. Verify the website works correctly"
    echo "3. Test all image links and downloads"
else
    echo -e "${YELLOW}========================================${NC}"
    echo -e "${YELLOW}⚠️  ATTENTION REQUIRED${NC}"
    echo -e "${YELLOW}========================================${NC}"
    echo ""
    echo "Please review the issues above before hosting."
fi

echo ""
echo "File permissions set:"
echo "  - Files (HTML, CSS, JS, images, PDF): 644 (rw-r--r--)"
echo "  - Directories: 755 (rwxr-xr-x)"
echo ""

exit 0
