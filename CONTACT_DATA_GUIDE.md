# Contact Page Data Management Guide

## Overview
The contact page (`contact.html`) now loads all its content dynamically from `contact.json`. This allows you to update contact information, form fields, and text without editing HTML.

## How to Update Contact Information

### 1. Edit contact.json
All contact page data is stored in `contact.json`. Simply edit this file to update:
- Page header text
- Contact information (address, phone, email)
- Form field labels and placeholders
- Inquiry type options
- Button text

### 2. JSON Structure

```json
{
  "pageHeader": {
    "badge": "Badge text",
    "title": "Main title with <span> tags allowed",
    "subtitle": "Subtitle description"
  },
  "contactInfo": {
    "address": {
      "icon": "📍",
      "title": "Visit Us",
      "line1": "770 E Elm Ave",
      "line2": "Coalinga, CA 93210",
      "googleMapsUrl": "https://www.google.com/maps/...",
      "buttonText": "Get Directions →"
    },
    "phone": {
      "icon": "📞",
      "title": "Call Us",
      "number": "(555) 555-1234",
      "phoneLink": "tel:+15555551234",
      "hours": "Mon-Fri: 9AM-6PM<br>Sat: 10AM-4PM"
    },
    "email": {
      "icon": "✉️",
      "title": "Email Us",
      "address": "rent@peppertreetownhomes.com",
      "emailLink": "mailto:rent@peppertreetownhomes.com",
      "responseTime": "We respond within 24 hours"
    }
  },
  "contactForm": {
    "header": "✨ Send Us a Message",
    "subtitle": "Form description",
    "fields": {
      "firstName": {
        "placeholder": "First Name *",
        "required": true
      },
      ...
    },
    "submitButton": "Send Message"
  }
}
```

## Common Updates

### Update Phone Number
```json
"phone": {
  "number": "(559) 123-4567",
  "phoneLink": "tel:+15591234567"
}
```
⚠️ **Important**: Make sure `phoneLink` uses the format `tel:+1XXXXXXXXXX` (no spaces, dashes, or parentheses)

### Update Email Address
```json
"email": {
  "address": "newemail@example.com",
  "emailLink": "mailto:newemail@example.com"
}
```

### Update Address
```json
"address": {
  "line1": "123 Main Street",
  "line2": "City, State ZIP",
  "googleMapsUrl": "https://www.google.com/maps/dir/?api=1&destination=YOUR+ADDRESS"
}
```
💡 **Tip**: Get Google Maps URL by:
1. Go to Google Maps
2. Search for your address
3. Click "Directions"
4. Copy the URL

### Update Business Hours
```json
"hours": "Monday-Friday: 8AM-5PM<br>Weekends: Closed"
```
⚠️ **Note**: Use `<br>` for line breaks in HTML fields

### Add/Remove Inquiry Types
```json
"inquiryType": {
  "options": [
    {
      "value": "tour",
      "label": "Scheduling a Tour"
    },
    {
      "value": "newtype",
      "label": "Your New Option"
    }
  ]
}
```

### Change Form Field Placeholders
```json
"fields": {
  "firstName": {
    "placeholder": "Enter Your First Name *",
    "required": true
  }
}
```

## Technical Details

### How It Works
1. When the page loads, JavaScript fetches `contact.json`
2. The script populates all elements with `data-field` attributes
3. Contact cards are generated dynamically
4. Form fields get their placeholders and options from JSON

### Files Involved
- **contact.json** - Data storage
- **contact.html** - Page structure and loader script
- HTML elements use `data-field` attributes to identify which data to load

### Troubleshooting

**Q: Changes don't appear**
- Hard refresh the page: `Ctrl+F5` (Windows/Linux) or `Cmd+Shift+R` (Mac)
- Check browser console (F12) for JavaScript errors
- Verify JSON syntax is valid (no missing commas, quotes, brackets)

**Q: Page shows blank**
- JSON file might have syntax error
- Use a JSON validator: https://jsonlint.com
- Check browser console for error messages

**Q: Links don't work**
- Verify `phoneLink` format: `tel:+1XXXXXXXXXX`
- Verify `emailLink` format: `mailto:email@example.com`
- Verify `googleMapsUrl` is a complete URL starting with `https://`

### JSON Syntax Rules
✅ DO:
- Use double quotes `"` for all strings
- Include commas between properties (except the last one)
- Keep brackets and braces balanced `{}` and `[]`

❌ DON'T:
- Use single quotes `'`
- Add comma after the last property in an object
- Forget to close brackets/braces

### Validation
Before saving changes, validate your JSON:
1. Copy the entire contents of `contact.json`
2. Paste into https://jsonlint.com
3. Click "Validate JSON"
4. Fix any errors shown

## Best Practices

1. **Always backup** `contact.json` before major changes
2. **Test changes** on a local server before deploying
3. **Validate JSON** after every edit
4. **Use consistent formatting** (icons, capitalization, punctuation)
5. **Keep phone/email formats** consistent throughout the file

## Example: Complete Update

To change phone, email, and hours:

```json
"phone": {
  "icon": "📞",
  "title": "Call Us",
  "number": "(559) 935-2525",
  "phoneLink": "tel:+15599352525",
  "hours": "Monday-Friday: 8:30AM-5:30PM<br>Saturday: 9AM-1PM<br>Sunday: Closed"
},
"email": {
  "icon": "✉️",
  "title": "Email Us",
  "address": "info@peppertreetownhomes.com",
  "emailLink": "mailto:info@peppertreetownhomes.com",
  "responseTime": "We respond within 12 hours during business days"
}
```

---

**Need Help?**
- Check the browser console (F12) for errors
- Validate JSON syntax at jsonlint.com
- Compare with the original backup file
