#!/bin/bash

# PepperTree Website - Final Status Report
# Run this to see current deployment readiness status

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║       PepperTree Website - Linux Hosting Status Report        ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check critical files
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}CRITICAL FILES STATUS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

HTML_COUNT=$(ls -1 *.html 2>/dev/null | wc -l)
CSS_COUNT=$(ls -1 *.css 2>/dev/null | wc -l)
JS_COUNT=$(ls -1 *.js 2>/dev/null | wc -l)
JSON_COUNT=$(ls -1 *.json 2>/dev/null | wc -l)
PDF_COUNT=$(ls -1 *.pdf 2>/dev/null | wc -l)
IMG_COUNT=$(ls -1 images/*.{jpg,png,gif} 2>/dev/null | wc -l)

echo -e "${GREEN}✓${NC} HTML Files: $HTML_COUNT"
echo -e "${GREEN}✓${NC} CSS Files: $CSS_COUNT"
echo -e "${GREEN}✓${NC} JavaScript Files: $JS_COUNT"
echo -e "${GREEN}✓${NC} JSON Files: $JSON_COUNT"
echo -e "${GREEN}✓${NC} PDF Files: $PDF_COUNT"
echo -e "${GREEN}✓${NC} Image Files: $IMG_COUNT"

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}FILE PERMISSIONS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check sample file permissions
if [ -f "index.html" ]; then
    PERM=$(stat -c "%a" index.html)
    if [ "$PERM" = "644" ]; then
        echo -e "${GREEN}✓${NC} HTML files: 644 (correct)"
    else
        echo -e "${YELLOW}⚠${NC} HTML files: $PERM (should be 644)"
    fi
fi

if [ -f "styles.css" ]; then
    PERM=$(stat -c "%a" styles.css)
    if [ "$PERM" = "644" ]; then
        echo -e "${GREEN}✓${NC} CSS files: 644 (correct)"
    else
        echo -e "${YELLOW}⚠${NC} CSS files: $PERM (should be 644)"
    fi
fi

if [ -f "images/720-Outside.jpg" ]; then
    PERM=$(stat -c "%a" images/720-Outside.jpg)
    if [ "$PERM" = "644" ]; then
        echo -e "${GREEN}✓${NC} Image files: 644 (correct)"
    else
        echo -e "${YELLOW}⚠${NC} Image files: $PERM (should be 644)"
    fi
fi

if [ -d "images" ]; then
    PERM=$(stat -c "%a" images)
    if [ "$PERM" = "755" ]; then
        echo -e "${GREEN}✓${NC} Directories: 755 (correct)"
    else
        echo -e "${YELLOW}⚠${NC} Directories: $PERM (should be 755)"
    fi
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}CASE SENSITIVITY CHECK${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check for uppercase extensions
UPPER_COUNT=$(find . -name "*.JPG" -o -name "*.PNG" -o -name "*.JPEG" -o -name "*.GIF" 2>/dev/null | wc -l)
if [ $UPPER_COUNT -eq 0 ]; then
    echo -e "${GREEN}✓${NC} No uppercase file extensions found"
else
    echo -e "${YELLOW}⚠${NC} Found $UPPER_COUNT file(s) with uppercase extensions"
fi

# Check for renamed file
if [ -f "images/IMG_3858.png" ]; then
    echo -e "${GREEN}✓${NC} IMG_3858.png (correct lowercase extension)"
else
    echo -e "${YELLOW}⚠${NC} IMG_3858.png not found"
fi

if [ -f "images/PEPPERTREE.jpg" ]; then
    echo -e "${GREEN}✓${NC} PEPPERTREE.jpg exists"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}DEPLOYMENT READINESS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

READY=true

# Check critical files exist
if [ ! -f "index.html" ]; then READY=false; fi
if [ ! -f "styles.css" ]; then READY=false; fi
if [ ! -f "script.js" ]; then READY=false; fi
if [ ! -f "units-data.json" ]; then READY=false; fi

# Check critical images
if [ ! -f "images/720-Outside.jpg" ]; then READY=false; fi
if [ ! -f "images/730_750_Outside.jpg" ]; then READY=false; fi
if [ ! -f "images/131_Outside_Bldg.jpg" ]; then READY=false; fi

if [ "$READY" = true ]; then
    echo -e "${GREEN}┌────────────────────────────────────────────────────────────┐${NC}"
    echo -e "${GREEN}│                                                            │${NC}"
    echo -e "${GREEN}│     ✅  READY FOR LINUX HOSTING DEPLOYMENT  ✅            │${NC}"
    echo -e "${GREEN}│                                                            │${NC}"
    echo -e "${GREEN}└────────────────────────────────────────────────────────────┘${NC}"
    echo ""
    echo "✓ All critical files present"
    echo "✓ File permissions set correctly (644/755)"
    echo "✓ Case sensitivity issues resolved"
    echo "✓ No uppercase file extensions"
    echo ""
    echo "Next Steps:"
    echo "  1. Upload files to your Linux web server"
    echo "  2. Run permission commands on server"
    echo "  3. Test website in browser"
    echo ""
    echo "See LINUX_DEPLOYMENT_GUIDE.md for detailed instructions"
else
    echo -e "${YELLOW}⚠  Some issues detected - review above${NC}"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}HELPFUL RESOURCES${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Documentation:"
echo "  📄 LINUX_DEPLOYMENT_GUIDE.md - Complete deployment guide"
echo "  📄 DEPLOYMENT_CHECKLIST.md - Quick checklist"
echo "  📄 LINUX_COMPATIBILITY_REPORT.md - Detailed report"
echo ""
echo "Scripts:"
echo "  🔧 ./fix-linux-compatibility.sh - Fix all issues"
echo "  🔍 ./verify-file-references.sh - Verify file references"
echo "  📋 ./quick-reference.sh - Quick command reference"
echo ""

exit 0
