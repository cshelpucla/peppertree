#!/bin/bash
# PepperTree Website - Linux Server Setup Script
# Run this script after uploading files to your Linux hosting server

echo "🐧 PepperTree Website - Linux Server Setup"
echo "========================================"

# Get the current directory (should be your website root)
WEBSITE_DIR=$(pwd)
echo "Setting up permissions in: $WEBSITE_DIR"

echo ""
echo "📁 Setting directory permissions (755)..."
find . -type d -exec chmod 755 {} \;
echo "✅ Directory permissions set"

echo ""
echo "📄 Setting HTML file permissions (644)..."
find . -name "*.html" -exec chmod 644 {} \;
echo "✅ HTML file permissions set"

echo ""
echo "🎨 Setting CSS file permissions (644)..."
find . -name "*.css" -exec chmod 644 {} \;
echo "✅ CSS file permissions set"

echo ""
echo "⚙️ Setting JavaScript file permissions (644)..."
find . -name "*.js" -exec chmod 644 {} \;
echo "✅ JavaScript file permissions set"

echo ""
echo "📋 Setting PDF file permissions (644)..."
find . -name "*.pdf" -exec chmod 644 {} \;
echo "✅ PDF file permissions set"

echo ""
echo "🖼️ Setting image file permissions (644)..."
find . -name "*.jpg" -exec chmod 644 {} \;
find . -name "*.jpeg" -exec chmod 644 {} \;
find . -name "*.png" -exec chmod 644 {} \;
find . -name "*.gif" -exec chmod 644 {} \;
echo "✅ Image file permissions set"

echo ""
echo "🔍 Checking for potential case sensitivity issues..."

# Check for common problematic files
if [ -f "images/IMG_3858.PNG" ]; then
    echo "⚠️  Found: IMG_3858.PNG (uppercase extension)"
    echo "   Consider renaming to: img_3858.png"
fi

if [ -f "images/PEPPERTREE.jpg" ]; then
    echo "⚠️  Found: PEPPERTREE.jpg (uppercase letters)"
    echo "   Consider renaming to: peppertree.jpg"
fi

echo ""
echo "📊 Permission Summary:"
echo "Directories: 755 (rwxr-xr-x)"
echo "Files: 644 (rw-r--r--)"

echo ""
echo "🔗 Testing basic file accessibility..."

# Test key files
if [ -f "index.html" ]; then
    echo "✅ index.html - accessible"
else
    echo "❌ index.html - MISSING!"
fi

if [ -f "styles.css" ]; then
    echo "✅ styles.css - accessible"
else
    echo "❌ styles.css - MISSING!"
fi

if [ -d "images" ]; then
    IMAGE_COUNT=$(find images -name "*.jpg" -o -name "*.png" | wc -l)
    echo "✅ images directory - $IMAGE_COUNT images found"
else
    echo "❌ images directory - MISSING!"
fi

echo ""
echo "🎉 Linux server setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Test your website in a browser"
echo "2. Check browser console for any 404 errors"
echo "3. Test the rental application forms"
echo "4. Verify all images load correctly"
echo ""
echo "🌐 Your PepperTree website should now be live on Linux hosting!"
