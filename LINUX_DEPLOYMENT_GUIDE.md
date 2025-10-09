# 🚀 PepperTree Website - Linux Hosting Deployment Guide

## ✅ PRE-DEPLOYMENT STATUS

**Status: READY FOR LINUX HOSTING** ✅

All file references and permissions have been corrected for Linux compatibility.

---

## 📋 WHAT WAS FIXED

### 1. **File Case Sensitivity Issues** ✅
- Renamed `IMG_3858.PNG` → `IMG_3858.png` (lowercase extension)
- Verified `PEPPERTREE.jpg` exists and is referenced correctly
- All HTML file references use correct case matching actual filenames

### 2. **File Permissions** ✅
All files now have proper Linux permissions:
- **HTML files**: 644 (rw-r--r--)
- **CSS files**: 644 (rw-r--r--)
- **JavaScript files**: 644 (rw-r--r--)
- **Image files** (jpg, png, gif): 644 (rw-r--r--)
- **PDF files**: 644 (rw-r--r--)
- **JSON files**: 644 (rw-r--r--)
- **Directories**: 755 (rwxr-xr-x)

### 3. **File References Verified** ✅
- All 56 image references in HTML files verified
- No broken links found
- No uppercase extension references in HTML
- All critical files present

---

## 📦 FILES TO UPLOAD

### **Core Website Files** (Required)
```
index.html
available.html
available-720c.html
available-730a.html
available-151a.html
floorplans.html
amenities.html
gallery.html
neighborhood.html
contact.html
rental-application.html
styles.css
script.js
units-data.json
unit-data-loader.js
unit-loader.js
home-units-loader.js
Golden_Hills_Rental_Application_Fillable.pdf
```

### **Images Directory** (Required)
Upload the entire `images/` folder with all subdirectories:
- 720C unit photos (13 images)
- 730A unit photos (5 images)
- 151A unit photos (1 image)
- Generic unit photos (7 images)
- Neighborhood photos (6 images)
- Building exterior photos (11 images)
- Banner images (3 images)

### **Optional Files** (Not needed for hosting)
```
*.py (Python scripts - for development only)
*.md (Documentation files)
*.sh (Setup scripts)
image-validator.html (utility file)
build.md
HOSTING_*.md
```

---

## 🚀 DEPLOYMENT STEPS

### **Step 1: Upload Files to Server**

#### Option A: FTP/SFTP Upload
1. Connect to your Linux web server via FTP/SFTP
2. Navigate to your web root directory (usually `/var/www/html` or `/public_html`)
3. Upload all files maintaining the directory structure:
   ```
   /
   ├── index.html
   ├── *.html (all HTML files)
   ├── styles.css
   ├── script.js
   ├── *.js (all JS files)
   ├── units-data.json
   ├── Golden_Hills_Rental_Application_Fillable.pdf
   └── images/
       └── (all image files)
   ```

#### Option B: SSH/SCP Upload
```bash
# From your local machine, upload to server
scp -r /home/cshelp/peppertree/* user@yourserver.com:/var/www/html/

# Or use rsync for better control
rsync -avz --exclude='*.py' --exclude='*.md' --exclude='*.sh' \
  /home/cshelp/peppertree/ user@yourserver.com:/var/www/html/
```

### **Step 2: Set Permissions on Server** ⚠️ CRITICAL

After uploading, SSH into your server and run:

```bash
# Navigate to your web directory
cd /var/www/html  # or your web root

# Set file permissions
find . -type f -name "*.html" -exec chmod 644 {} \;
find . -type f -name "*.css" -exec chmod 644 {} \;
find . -type f -name "*.js" -exec chmod 644 {} \;
find . -type f -name "*.json" -exec chmod 644 {} \;
find . -type f -name "*.pdf" -exec chmod 644 {} \;
find . -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.gif" \) -exec chmod 644 {} \;

# Set directory permissions
find . -type d -exec chmod 755 {} \;

# Quick alternative (set all at once):
chmod 644 *.html *.css *.js *.json *.pdf
chmod 644 images/*
chmod 755 images/
chmod 755 .
```

### **Step 3: Verify Deployment**

1. **Test the Homepage**
   - Navigate to: `http://yourdomain.com/`
   - Check that it loads without errors

2. **Check Browser Console**
   - Open Developer Tools (F12)
   - Check Console for any 404 errors
   - Check Network tab for failed image loads

3. **Test All Pages**
   - Click through all navigation links
   - Verify images load on each page:
     - Home
     - Floor Plans
     - Amenities
     - Gallery
     - Neighborhood
     - Available Units (all variants)
     - Rental Application
     - Contact

4. **Test Downloads**
   - Test PDF download: `Golden_Hills_Rental_Application_Fillable.pdf`
   - Should download without errors

5. **Test Mobile View**
   - Resize browser or test on mobile device
   - Verify responsive layout works

### **Step 4: Test Image Loading**

Critical images to verify:
- `images/720-Outside.jpg` (Unit 720C)
- `images/730_750_Outside.jpg` (Unit 730A)
- `images/131_Outside_Bldg.jpg` (Unit 151A)
- `images/unit-1-exterior.jpg`
- `images/720C_LivingRoom.jpg`
- All neighborhood images

---

## 🔧 TROUBLESHOOTING

### **Problem: Images not loading (404 errors)**

**Cause**: Case sensitivity or incorrect file permissions

**Solution**:
1. Check file exists with exact name: `ls -la images/filename.jpg`
2. Verify file permissions: should be 644
3. Check HTML reference matches exact filename (case-sensitive)
4. Run: `chmod 644 images/*.jpg images/*.png`

### **Problem: Permission Denied errors**

**Solution**:
```bash
# Set correct permissions
chmod 755 /var/www/html
chmod 755 /var/www/html/images
chmod 644 /var/www/html/*.html
chmod 644 /var/www/html/images/*
```

### **Problem: index.html not showing as default page**

**Solution**: Check Apache/Nginx configuration
- Apache: Ensure `DirectoryIndex index.html` is set
- Nginx: Ensure `index index.html;` is in server block

---

## ✅ POST-DEPLOYMENT CHECKLIST

- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] All images display properly
- [ ] PDF downloads work
- [ ] Rental application form displays
- [ ] Contact information displays correctly
- [ ] Mobile view works properly
- [ ] No console errors in browser
- [ ] All unit pages load (720C, 730A, 151A)
- [ ] Gallery images load
- [ ] Neighborhood page works

---

## 📊 FILE STATISTICS

- **Total HTML files**: 12
- **Total image files**: 50+
- **Total CSS files**: 1
- **Total JS files**: 4
- **Total PDF files**: 1
- **Total JSON files**: 1

---

## 🔐 SECURITY NOTES

### **File Permissions Explained**
- **644** (rw-r--r--): Owner can read/write, others can only read
- **755** (rwxr-xr-x): Owner can read/write/execute, others can read/execute

### **Why These Permissions?**
- Files (644): Web server can read, users can download, but cannot execute
- Directories (755): Web server can list contents, users can browse
- No files are executable (prevents security issues)

---

## 📞 SUPPORT

If you encounter issues after deployment:

1. Check server error logs: `/var/log/apache2/error.log` or `/var/log/nginx/error.log`
2. Verify file ownership: `ls -la` (should be owned by web server user)
3. Test file access: `curl http://yourdomain.com/images/720-Outside.jpg`
4. Use browser DevTools to identify specific issues

---

## 🎉 SUCCESS CRITERIA

Your website is successfully deployed when:
- ✅ All pages load without errors
- ✅ All images display correctly
- ✅ Navigation works smoothly
- ✅ Forms are functional
- ✅ Downloads work
- ✅ Mobile view looks good
- ✅ No console errors

---

**Last Updated**: Auto-generated after Linux compatibility fixes
**Status**: Production Ready ✅
