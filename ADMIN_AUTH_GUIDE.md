# Admin Authentication System Guide

## Overview
The PepperTree Townhomes website now includes a complete admin authentication and user management system. This system protects administrative pages (like the applications list) and allows administrators to manage user accounts.

## Features
- **Session-based authentication** using PHP sessions
- **Role-based access control** (administrator vs user roles)
- **User management interface** for adding/removing admin accounts
- **Modal-based UI** for login and user management
- **Secure password handling** (backend validation)
- **Persistent sessions** across page refreshes

## Default Admin Account
- **Username:** `admin`
- **Password:** `admin123`
- **Email:** admin@peppertreetownhomes.com
- **Role:** Administrator

**⚠️ IMPORTANT:** Change the default password immediately after first login!

## Files & Structure

### Backend Files
1. **users.json** - User database (JSON format)
   - Stores: username, password, email, role, createdAt, lastLogin
   - Located in root directory

2. **auth.php** - Authentication API
   - POST: Login with username/password
   - GET: Check current session status
   - DELETE: Logout and destroy session

3. **manage_users.php** - User management API (admin only)
   - GET: List all users (passwords excluded)
   - POST: Create new user
   - DELETE: Remove user (prevents self-deletion)

### Frontend Files
1. **admin-auth.js** - Authentication JavaScript
   - Login/logout functionality
   - User management (add, list, delete)
   - Session checking on page load
   - Modal controls
   - Notification system

2. **admin-auth.css** - Authentication styles
   - Auth button styling (top right corner)
   - Modal designs (login, user management, add user)
   - Table styling for users list
   - Responsive design

### Integrated Pages
- **applications-list.html** - Applications dashboard with auth
- **view-application.html** - Individual application viewer with auth

## How It Works

### Sign In Process
1. User clicks "🔐 Sign In" button (top right corner)
2. Login modal appears with username/password fields
3. Credentials are validated against `users.json`
4. On success:
   - PHP session is created
   - `lastLogin` timestamp is updated
   - Button changes to "👤 [username]"
   - User gains access to admin features

### User Management
1. Admin clicks on username button → Admin menu appears
2. Clicks "👥 Manage Users" → User management modal opens
3. View all users with:
   - Username, email, role
   - Created date, last login
   - Delete button (except for current user)

### Adding New Users
1. In User Management modal, click "➕ Add User"
2. Fill out form:
   - Username (3+ characters, must be unique)
   - Email (valid email format)
   - Password (6+ characters minimum)
   - Role (Administrator or User)
3. Click "Save User" → New account is created
4. New entry added to `users.json`

### Logout
1. Click username button → Admin menu
2. Click "🚪 Logout"
3. Session destroyed
4. Returns to "🔐 Sign In" button

## Security Features
- **Session-based authentication**: Uses PHP `$_SESSION` for secure state management
- **Role-based access control**: User management requires administrator role
- **Duplicate username prevention**: Cannot create multiple accounts with same username
- **Self-deletion protection**: Admins cannot delete their own account
- **Password validation**: Minimum length requirements enforced
- **HTTP status codes**: Proper error handling (400, 401, 403, 500)

## API Endpoints

### POST /auth.php
**Login authentication**
```json
Request:
{
  "username": "admin",
  "password": "admin123"
}

Response (200 OK):
{
  "success": true,
  "user": {
    "id": "1",
    "username": "admin",
    "email": "admin@peppertreetownhomes.com",
    "role": "administrator"
  }
}

Response (401 Unauthorized):
{
  "success": false,
  "message": "Invalid username or password"
}
```

### GET /auth.php
**Check session status**
```json
Response (authenticated):
{
  "authenticated": true,
  "user": { ... }
}

Response (not authenticated):
{
  "authenticated": false
}
```

### DELETE /auth.php
**Logout**
```json
Response (200 OK):
{
  "success": true,
  "message": "Logged out successfully"
}
```

### GET /manage_users.php
**List all users (admin only)**
```json
Response (200 OK):
{
  "success": true,
  "users": [
    {
      "id": "1",
      "username": "admin",
      "email": "admin@peppertreetownhomes.com",
      "role": "administrator",
      "createdAt": "2025-10-20T00:00:00-04:00",
      "lastLogin": "2025-10-20T14:30:00-04:00"
    }
  ],
  "count": 1
}

Response (403 Forbidden):
{
  "success": false,
  "message": "Administrator access required"
}
```

### POST /manage_users.php
**Create new user (admin only)**
```json
Request:
{
  "username": "newadmin",
  "email": "newadmin@example.com",
  "password": "password123",
  "role": "administrator"
}

Response (201 Created):
{
  "success": true,
  "message": "User created successfully",
  "userId": "2"
}

Response (400 Bad Request):
{
  "success": false,
  "message": "Username already exists"
}
```

### DELETE /manage_users.php?id=2
**Delete user (admin only)**
```json
Response (200 OK):
{
  "success": true,
  "message": "User deleted successfully"
}

Response (400 Bad Request):
{
  "success": false,
  "message": "Cannot delete your own account"
}
```

## Usage Instructions

### For End Users (Admins)
1. **First-time setup:**
   - Navigate to applications-list.html
   - Click "🔐 Sign In" button
   - Login with default credentials (admin/admin123)
   - Go to Manage Users → click your username → Add new password

2. **Daily use:**
   - Sign in when accessing admin pages
   - Session persists while browser is open
   - Can manage applications without re-authenticating
   - Sign out when finished

3. **Adding team members:**
   - Sign in as administrator
   - Click username → "👥 Manage Users"
   - Click "➕ Add User"
   - Fill in details and select role
   - New user receives credentials via email (manual process)

### For Developers
1. **Adding auth to new pages:**
   ```html
   <!-- In <head> -->
   <link rel="stylesheet" href="admin-auth.css">
   
   <!-- Before </body> -->
   <button id="authButton">🔐 Sign In</button>
   <div id="adminMenu">...</div>
   <!-- Include all modals (login, user mgmt, add user) -->
   <script src="admin-auth.js"></script>
   ```

2. **Checking auth in JavaScript:**
   ```javascript
   // admin-auth.js provides global currentUser variable
   if (currentUser && currentUser.role === 'administrator') {
       // Show admin-only features
   }
   ```

3. **Protecting PHP endpoints:**
   ```php
   session_start();
   if (!isset($_SESSION['user'])) {
       http_response_code(401);
       echo json_encode(['error' => 'Unauthorized']);
       exit;
   }
   ```

## Testing Checklist
- [ ] Can login with default admin credentials
- [ ] Session persists across page navigation
- [ ] Can access user management
- [ ] Can add new users
- [ ] Cannot add duplicate usernames
- [ ] Can delete other users (not self)
- [ ] Can logout successfully
- [ ] Sign in button reappears after logout
- [ ] Modal close buttons work
- [ ] Form validation works (min lengths, email format)
- [ ] Notifications appear for success/error

## Troubleshooting

### "Failed to load users"
- Check that `users.json` exists and is readable
- Verify PHP has write permissions to the file
- Check browser console for detailed errors

### "Session not persisting"
- Ensure PHP session is enabled in php.ini
- Check that cookies are enabled in browser
- Verify session_start() is called in auth.php

### "Cannot add user"
- Check username isn't already taken
- Verify all required fields are filled
- Check users.json file permissions (must be writable)

### "Unauthorized" errors
- Clear browser cache and cookies
- Log out and log back in
- Check that session hasn't expired

## Future Enhancements
- [ ] Password reset functionality
- [ ] Email notifications for new accounts
- [ ] Two-factor authentication (2FA)
- [ ] Activity logging / audit trail
- [ ] Password strength requirements
- [ ] Account lockout after failed attempts
- [ ] Remember me functionality
- [ ] Profile editing for users
- [ ] Bulk user import/export

## Security Notes
⚠️ **IMPORTANT:** This is a basic authentication system suitable for small internal tools. For production use with sensitive data, consider:
- Hashing passwords (bcrypt, argon2)
- HTTPS/SSL encryption
- CSRF protection
- Rate limiting on login attempts
- More robust session management
- Regular security audits
- Compliance with data protection regulations

## Support
For questions or issues, contact the development team or refer to the main README.md file.
