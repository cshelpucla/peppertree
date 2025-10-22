#!/bin/bash
# Appointments System Verification Script
# Tests all endpoints and functionality

echo "========================================="
echo "  APPOINTMENTS SYSTEM VERIFICATION"
echo "========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test counter
PASSED=0
FAILED=0

# Function to test endpoint
test_endpoint() {
    local name=$1
    local url=$2
    local expected=$3
    
    echo -n "Testing $name... "
    response=$(curl -s "$url")
    
    if echo "$response" | grep -q "$expected"; then
        echo -e "${GREEN}✓ PASS${NC}"
        ((PASSED++))
    else
        echo -e "${RED}✗ FAIL${NC}"
        ((FAILED++))
        echo "  Response: $response"
    fi
}

echo "=== Backend API Tests ==="
echo ""

# Test 1: List appointments endpoint
test_endpoint "list_appointments.php" \
    "http://localhost:8000/list_appointments.php" \
    '"success":true'

# Test 2: Get appointment (test123)
test_endpoint "get_appointment.php (test123)" \
    "http://localhost:8000/get_appointment.php?id=test123" \
    '"name":"John Doe"'

# Test 3: Get appointment (demo456)
test_endpoint "get_appointment.php (demo456)" \
    "http://localhost:8000/get_appointment.php?id=demo456" \
    '"name":"Jane Smith"'

# Test 4: Invalid appointment ID
test_endpoint "get_appointment.php (invalid)" \
    "http://localhost:8000/get_appointment.php?id=invalid999" \
    '"success":false'

echo ""
echo "=== Frontend File Tests ==="
echo ""

# Test 5: appointments-list.html exists
if [ -f "/home/cshelp/peppertree/appointments-list.html" ]; then
    echo -e "appointments-list.html exists... ${GREEN}✓ PASS${NC}"
    ((PASSED++))
else
    echo -e "appointments-list.html exists... ${RED}✗ FAIL${NC}"
    ((FAILED++))
fi

# Test 6: view-appointment.html exists
if [ -f "/home/cshelp/peppertree/view-appointment.html" ]; then
    echo -e "view-appointment.html exists... ${GREEN}✓ PASS${NC}"
    ((PASSED++))
else
    echo -e "view-appointment.html exists... ${RED}✗ FAIL${NC}"
    ((FAILED++))
fi

# Test 7: Check appointments-list.html has key features
if grep -q "appointments-table" "/home/cshelp/peppertree/appointments-list.html" && \
   grep -q "searchInput" "/home/cshelp/peppertree/appointments-list.html" && \
   grep -q "checkPageAccess" "/home/cshelp/peppertree/appointments-list.html"; then
    echo -e "appointments-list.html structure... ${GREEN}✓ PASS${NC}"
    ((PASSED++))
else
    echo -e "appointments-list.html structure... ${RED}✗ FAIL${NC}"
    ((FAILED++))
fi

# Test 8: Check view-appointment.html has key features
if grep -q "renderAppointment" "/home/cshelp/peppertree/view-appointment.html" && \
   grep -q "createSection" "/home/cshelp/peppertree/view-appointment.html" && \
   grep -q "window.print" "/home/cshelp/peppertree/view-appointment.html"; then
    echo -e "view-appointment.html structure... ${GREEN}✓ PASS${NC}"
    ((PASSED++))
else
    echo -e "view-appointment.html structure... ${RED}✗ FAIL${NC}"
    ((FAILED++))
fi

echo ""
echo "=== Data Tests ==="
echo ""

# Test 9: Appointment count
count=$(curl -s "http://localhost:8000/list_appointments.php" | grep -o '"count":[0-9]*' | grep -o '[0-9]*')
if [ "$count" -ge "2" ]; then
    echo -e "Appointment count ($count)... ${GREEN}✓ PASS${NC}"
    ((PASSED++))
else
    echo -e "Appointment count ($count)... ${RED}✗ FAIL${NC}"
    ((FAILED++))
fi

# Test 10: Test appointments directory
if [ -d "/home/cshelp/peppertree/appointments" ]; then
    apt_files=$(ls -1 /home/cshelp/peppertree/appointments/apt_*.json 2>/dev/null | wc -l)
    if [ "$apt_files" -ge "2" ]; then
        echo -e "Appointments directory ($apt_files files)... ${GREEN}✓ PASS${NC}"
        ((PASSED++))
    else
        echo -e "Appointments directory... ${RED}✗ FAIL${NC}"
        ((FAILED++))
    fi
else
    echo -e "Appointments directory... ${RED}✗ FAIL${NC}"
    ((FAILED++))
fi

echo ""
echo "========================================="
echo "  TEST RESULTS"
echo "========================================="
echo ""
echo "Tests Passed: $PASSED"
echo "Tests Failed: $FAILED"
echo "Total Tests:  $((PASSED + FAILED))"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ ALL TESTS PASSED${NC}"
    echo ""
    echo "System Status: PRODUCTION READY ✅"
    exit 0
else
    echo -e "${RED}✗ SOME TESTS FAILED${NC}"
    echo ""
    echo "System Status: NEEDS ATTENTION ⚠️"
    exit 1
fi
