# Appointments System - Quick Reference Guide

## 🎯 Overview
The appointments viewing system allows administrators to view and manage tour appointment requests submitted through the website's scheduling form.

---

## 📁 Files Structure

```
peppertree/
├── appointments-list.html          # Main list view (admin)
├── view-appointment.html           # Detail view (admin)
├── list_appointments.php           # Backend: List all
├── get_appointment.php             # Backend: Get one
├── schedule-handler.php            # Creates appointments (from form)
└── appointments/
    ├── apt_test123.json           # Example appointment 1
    └── apt_demo456.json           # Example appointment 2
```

---

## 🚀 How to Use

### For Administrators

#### 1. Access the Appointments List
1. Log in as admin
2. Click "Appointments" in the navigation menu
3. You'll see:
   - **Stats Cards**: Total, Today, This Week
   - **Search Bar**: Filter by name, email, or phone
   - **Sort Dropdown**: Newest/Oldest/Name A-Z/Z-A
   - **Table**: All appointments with action buttons

#### 2. View Appointment Details
1. Click the "👁️ View" button on any appointment
2. You'll see:
   - Submission date and ID
   - Contact information (name, email, phone)
   - Tour details (which unit they're interested in)
   - Preferred time slots (all options they selected)
   - Additional notes (if provided)
3. **Actions Available:**
   - Click "← Back to List" to return
   - Click "🖨️ Print" to print the appointment

#### 3. Search and Filter
- Type in the search box to filter by:
  - Visitor name
  - Email address
  - Phone number
- Results update instantly

#### 4. Sort Appointments
Select from dropdown:
- **Newest First**: Most recent submissions first (default)
- **Oldest First**: Earliest submissions first
- **Name A-Z**: Alphabetical order
- **Name Z-A**: Reverse alphabetical

---

## 🔧 For Developers

### Backend API Endpoints

#### List All Appointments
```bash
GET /list_appointments.php
```
**Response:**
```json
{
  "success": true,
  "appointments": [
    {
      "id": "apt_XXXXX",
      "submitted_at": "2025-10-22 00:40:00",
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "(555) 123-4567",
      "unit": "720c",
      "unit_text": "Unit 720C - 3BR Premium",
      "time_slots": [...]
    }
  ],
  "count": 1
}
```

#### Get Single Appointment
```bash
GET /get_appointment.php?id=XXXXX
```
**Response:**
```json
{
  "success": true,
  "appointment": {
    "id": "apt_XXXXX",
    "submitted_at": "2025-10-22 00:40:00",
    "contact": {
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "(555) 123-4567"
    },
    "tour_details": {
      "unit": "720c",
      "unit_text": "Unit 720C - 3BR Premium"
    },
    "time_slots": [
      {
        "priority": 1,
        "date": "2025-10-25",
        "time_hour": "10",
        "time_period": "AM",
        "formatted": "Friday, October 25, 2025 at 10:00 AM"
      }
    ],
    "notes": "Optional notes",
    "status": "pending"
  }
}
```

### Frontend Functions

#### appointments-list.html
```javascript
// Main functions
loadAppointments()           // Fetch and display all appointments
updateStats()                // Calculate and display statistics
renderAppointments()         // Render table rows
filterAppointments()         // Client-side search/filter
sortAppointments()           // Client-side sorting
checkPageAccess()           // Authentication check
```

#### view-appointment.html
```javascript
// Main functions
loadAppointment()           // Fetch appointment by ID
renderAppointment(apt)      // Display appointment details
createSection(title, fields) // Helper: Create section
createField(label, value)   // Helper: Create field
checkPageAccess()          // Authentication check
```

---

## 🔄 Auto-Refresh

The appointments list automatically refreshes every **30 seconds** in the background. This ensures you always see the latest submissions without manually refreshing the page.

---

## 📱 Mobile Support

Both pages are fully responsive:
- On desktop: Full table with all columns
- On mobile: Stacked layout, scrollable table
- On print: Clean, printer-friendly format

---

## 🔐 Security

- **Authentication Required**: Only logged-in admins can access
- **Auto-Redirect**: Non-authenticated users sent to homepage
- **Input Validation**: All IDs sanitized on backend
- **Directory Protection**: Prevents path traversal attacks

---

## 🎨 Customization

### Change Colors
Edit the `<style>` section in the HTML files:
```css
/* Main theme color */
#2c5530  /* Dark green */
#4a7c59  /* Light green */
```

### Add/Remove Columns
In `appointments-list.html`, modify the `renderAppointments()` function:
```javascript
// Add a new column in the table
return `
    <tr>
        <td>${formattedDate}</td>
        <td><strong>${name}</strong></td>
        <!-- Add your column here -->
        <td>...</td>
    </tr>
`;
```

### Modify Detail View
In `view-appointment.html`, edit the `renderAppointment()` function:
```javascript
// Add a new section
html += createSection('🆕 New Section', [
    { label: 'Field Name', value: apt.fieldName }
]);
```

---

## 🐛 Troubleshooting

### Appointments Not Loading
1. Check server is running: `ps aux | grep "php -S"`
2. Test endpoint: `curl http://localhost:8000/list_appointments.php`
3. Check browser console for errors
4. Verify `appointments/` directory exists

### Authentication Issues
1. Make sure you're logged in as admin
2. Check `admin-auth.js` is loading
3. Verify `auth.php` is accessible
4. Check browser console for auth errors

### Empty List
1. Check `appointments/` directory for JSON files
2. Files must start with `apt_` and end with `.json`
3. Verify JSON format is valid
4. Check file permissions (should be readable)

---

## 📊 Testing

Run the verification script:
```bash
cd /home/cshelp/peppertree
./verify-appointments-system.sh
```

This tests:
- Backend API endpoints
- Frontend file structure
- Data integrity
- File system setup

---

## 📝 Pattern Notes

This system follows the **exact same pattern** as the applications viewer:
- Same authentication flow
- Same list/detail structure
- Same styling and colors
- Same search/filter/sort functionality
- Same mobile responsiveness

**Why?** Consistency across admin interfaces makes the system easier to use and maintain.

---

## 🚀 Quick Start

1. **Start Server** (if not running):
   ```bash
   cd /home/cshelp/peppertree
   php -S localhost:8000
   ```

2. **Open Browser**:
   ```
   http://localhost:8000
   ```

3. **Log In** as admin

4. **Navigate** to Appointments

5. **Done!** 🎉

---

## 📞 Support

For issues or questions:
1. Check the test report: `APPOINTMENTS_SYSTEM_TEST_REPORT.md`
2. Review implementation: `APPOINTMENTS_IMPLEMENTATION_COMPLETE.md`
3. Run verification: `./verify-appointments-system.sh`

---

*Last Updated: October 22, 2025*
*Version: 1.0.0*
*Status: Production Ready ✅*
