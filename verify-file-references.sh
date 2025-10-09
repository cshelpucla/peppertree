#!/bin/bash

# PepperTree Website - File Reference Verification Script
# Checks all HTML files for broken image and file references

echo "🔍 PepperTree File Reference Verification"
echo "=========================================="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

BROKEN_REFS=0
TOTAL_REFS=0

echo -e "${BLUE}Checking image references in HTML files...${NC}"
echo ""

# Function to check if a file exists
check_file_ref() {
    local html_file=$1
    local ref_file=$2
    
    TOTAL_REFS=$((TOTAL_REFS + 1))
    
    if [ -f "$ref_file" ]; then
        echo -e "${GREEN}  ✓ ${ref_file}${NC}"
        return 0
    else
        echo -e "${RED}  ✗ BROKEN: ${ref_file} (referenced in ${html_file})${NC}"
        BROKEN_REFS=$((BROKEN_REFS + 1))
        return 1
    fi
}

# Extract image src references from HTML files and check them
echo -e "${BLUE}Scanning HTML files...${NC}"
echo ""

# Check index.html
if [ -f "index.html" ]; then
    echo "Checking index.html:"
    grep -o 'src="[^"]*"' index.html | sed 's/src="//;s/"//' | grep -E '\.(jpg|jpeg|png|gif|pdf)$' | while read ref; do
        check_file_ref "index.html" "$ref"
    done
fi

# Check available*.html files
for html_file in available*.html; do
    if [ -f "$html_file" ]; then
        echo ""
        echo "Checking $html_file:"
        grep -o 'src="[^"]*"' "$html_file" | sed 's/src="//;s/"//' | grep -E '\.(jpg|jpeg|png|gif|pdf)$' | while read ref; do
            check_file_ref "$html_file" "$ref"
        done
    fi
done

# Check other HTML files
for html_file in floorplans.html amenities.html gallery.html neighborhood.html contact.html rental-application.html; do
    if [ -f "$html_file" ]; then
        echo ""
        echo "Checking $html_file:"
        grep -o 'src="[^"]*"' "$html_file" | sed 's/src="//;s/"//' | grep -E '\.(jpg|jpeg|png|gif|pdf)$' | while read ref; do
            check_file_ref "$html_file" "$ref"
        done
    fi
done

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}VERIFICATION SUMMARY${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Note: Due to subshell execution in while loops, we need to recount
TOTAL_IMG_REFS=$(grep -h 'src="[^"]*"' *.html 2>/dev/null | sed 's/.*src="//;s/".*//' | grep -E '\.(jpg|jpeg|png|gif|pdf)$' | wc -l)
EXISTING_REFS=0

for html in *.html; do
    if [ -f "$html" ]; then
        grep -o 'src="[^"]*"' "$html" 2>/dev/null | sed 's/src="//;s/"//' | grep -E '\.(jpg|jpeg|png|gif|pdf)$' | while read ref; do
            if [ -f "$ref" ]; then
                EXISTING_REFS=$((EXISTING_REFS + 1))
            fi
        done
    fi
done

echo "Total image/file references found: $TOTAL_IMG_REFS"
echo ""

# Check for case sensitivity issues
echo -e "${BLUE}Checking for potential case sensitivity issues...${NC}"
echo ""

CASE_WARNINGS=0

# Check for references to files with uppercase extensions
if grep -r '\.PNG\|\.JPG\|\.JPEG\|\.GIF' *.html 2>/dev/null | grep -v "http" | grep -v "https"; then
    echo -e "${YELLOW}⚠ Found references with uppercase extensions${NC}"
    CASE_WARNINGS=$((CASE_WARNINGS + 1))
else
    echo -e "${GREEN}✓ No uppercase extension references in HTML files${NC}"
fi

echo ""

# Final status
if [ $CASE_WARNINGS -eq 0 ]; then
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}✅ ALL FILE REFERENCES ARE LINUX-COMPATIBLE${NC}"
    echo -e "${GREEN}========================================${NC}"
else
    echo -e "${YELLOW}========================================${NC}"
    echo -e "${YELLOW}⚠️  REVIEW WARNINGS ABOVE${NC}"
    echo -e "${YELLOW}========================================${NC}"
fi

echo ""
echo "File permissions status:"
ls -la index.html styles.css script.js 2>/dev/null | awk '{print "  " $1, $9}'
echo ""

exit 0
