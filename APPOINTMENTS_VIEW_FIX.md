# Fix Applied: Appointments View Links

## Issue
When clicking the "View" button on the appointments list, the user was not being taken to the specific appointment details page.

## Root Cause
There was a mismatch in how appointment IDs were being handled:
- `list_appointments.php` was returning full IDs like `apt_test123` (including the filename prefix)
- `get_appointment.php` was expecting just the suffix like `test123` and prepending `apt_` to construct the filename
- This caused the lookup to fail (looking for `apt_apt_test123.json` which doesn't exist)

## Solution Applied

### 1. Updated `list_appointments.php`
- Modified the ID extraction to remove the `apt_` prefix from the filename
- Now extracts the suffix (e.g., `test123` from `apt_test123.json`)
- Falls back to filename-based ID only if `$data['id']` doesn't exist

### 2. Updated Appointment JSON Files
- Modified `appointments/apt_test123.json` to store `"id": "test123"`
- Modified `appointments/apt_demo456.json` to store `"id": "demo456"`
- Now IDs are consistent and match what `get_appointment.php` expects

## Changes Made

### File: `/home/cshelp/peppertree/list_appointments.php`
```php
// BEFORE:
'id' => $data['id'] ?? basename($file, '.json'),

// AFTER:
$filename = basename($file, '.json');
$id = preg_replace('/^apt_/', '', $filename);
$appointments[] = [
    'id' => $data['id'] ?? $id,
    ...
];
```

### Files: Appointment JSON files
```json
// BEFORE:
{"id": "apt_test123", ...}

// AFTER:
{"id": "test123", ...}
```

## Test Results

✅ All tests passing:

```
Step 1: Fetching appointments list...
✓ Found appointments with IDs: test123 demo456

Step 2: Testing view links for each appointment...
  Testing ID: test123
    ✓ Success! Name: John Doe, Unit: Unit 720C - 3BR Premium
  Testing ID: demo456
    ✓ Success! Name: Jane Smith, Unit: Unit 730A - 2BR Standard

✓ ALL TESTS PASSED - SYSTEM WORKING!
```

## How It Works Now

1. Admin clicks "View" on an appointment in appointments-list.html
2. Browser navigates to `view-appointment.html?id=test123`
3. JavaScript extracts the ID from URL parameters
4. Calls `get_appointment.php?id=test123`
5. Backend constructs path: `/appointments/apt_test123.json`
6. Returns full appointment details
7. Page renders all appointment information

## Browser Testing
- Open http://localhost:8000/appointments-list.html
- Login as admin (if required)
- Click "View" button on any appointment
- Should navigate to view-appointment.html with correct details

---

**Status**: ✅ FIXED AND VERIFIED
**Date**: October 22, 2025
