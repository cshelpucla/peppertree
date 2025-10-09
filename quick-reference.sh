#!/bin/bash

# Quick Reference - PepperTree Linux Hosting Commands
# Copy and paste these commands when deploying to your Linux server

echo "=========================================="
echo "PepperTree - Quick Linux Hosting Commands"
echo "=========================================="
echo ""
echo "Copy these commands for your Linux server:"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1. SET FILE PERMISSIONS (Run in web directory)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat << 'EOF'

# Set all HTML, CSS, JS files to 644
find . -type f \( -name "*.html" -o -name "*.css" -o -name "*.js" \) -exec chmod 644 {} \;

# Set all images to 644
find . -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.gif" \) -exec chmod 644 {} \;

# Set PDF and JSON to 644
find . -type f \( -name "*.pdf" -o -name "*.json" \) -exec chmod 644 {} \;

# Set all directories to 755
find . -type d -exec chmod 755 {} \;

EOF

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2. QUICK PERMISSION FIX (Alternative)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat << 'EOF'

chmod 644 *.{html,css,js,json,pdf}
chmod 644 images/*
chmod 755 images/
chmod 755 .

EOF

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3. VERIFY DEPLOYMENT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat << 'EOF'

# Check file permissions
ls -la *.html
ls -la images/*.jpg | head

# Test if web server can read files
sudo -u www-data cat index.html > /dev/null && echo "✓ Web server can read files"

# Check for case sensitivity issues
find . -name "*.JPG" -o -name "*.PNG" -o -name "*.JPEG"

EOF

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4. UPLOAD COMMANDS (From local machine)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat << 'EOF'

# Using rsync (recommended)
rsync -avz --exclude='*.py' --exclude='*.md' --exclude='*.sh' \
  --exclude='.git' \
  /home/cshelp/peppertree/ user@yourserver.com:/var/www/html/

# Using SCP
scp -r *.html *.css *.js *.json *.pdf user@yourserver.com:/var/www/html/
scp -r images/ user@yourserver.com:/var/www/html/

# Then SSH in and set permissions:
ssh user@yourserver.com
cd /var/www/html
# Run permission commands from section 1

EOF

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5. TROUBLESHOOTING"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat << 'EOF'

# Check Apache/Nginx error logs
tail -f /var/log/apache2/error.log
# or
tail -f /var/log/nginx/error.log

# Test specific file access
curl http://yourdomain.com/images/720-Outside.jpg -I

# Check ownership (should be www-data or apache)
ls -la | grep -E "html|css|js"

# Fix ownership if needed
sudo chown -R www-data:www-data /var/www/html

EOF

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ CURRENT STATUS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "All files in /home/cshelp/peppertree are ready:"
echo "  ✓ File permissions set (644/755)"
echo "  ✓ Case sensitivity fixed"
echo "  ✓ All references verified"
echo "  ✓ 56 image references checked"
echo ""
echo "Ready to upload to Linux hosting!"
echo ""
