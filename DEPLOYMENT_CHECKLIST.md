# 📋 LINUX HOSTING - QUICK CHECKLIST

## ✅ PRE-UPLOAD CHECKLIST (Already Complete!)

- [x] File permissions set to 644/755
- [x] Case sensitivity issues fixed (IMG_3858.PNG → IMG_3858.png)
- [x] All file references verified (56 image references)
- [x] No broken links found
- [x] All critical files present
- [x] All critical images present

---

## 📤 UPLOAD CHECKLIST

Upload these files to your Linux web server:

### **Required Files:**
- [ ] All *.html files (12 files)
- [ ] styles.css
- [ ] script.js
- [ ] unit-data-loader.js
- [ ] unit-loader.js
- [ ] home-units-loader.js
- [ ] units-data.json
- [ ] Golden_Hills_Rental_Application_Fillable.pdf
- [ ] images/ folder (with all subdirectories)

### **Optional Files (Don't Upload):**
- Python scripts (*.py)
- Documentation (*.md)
- Setup scripts (*.sh)
- Development files

---

## 🔧 POST-UPLOAD CHECKLIST

After uploading to server, SSH in and run:

### **1. Set Permissions** ⚠️ CRITICAL
```bash
cd /var/www/html  # or your web root

# Quick method:
find . -type f -name "*.html" -exec chmod 644 {} \;
find . -type f -name "*.css" -exec chmod 644 {} \;
find . -type f -name "*.js" -exec chmod 644 {} \;
find . -type f -name "*.jpg" -exec chmod 644 {} \;
find . -type f -name "*.png" -exec chmod 644 {} \;
find . -type f -name "*.pdf" -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;
```

- [ ] Permissions set for HTML files
- [ ] Permissions set for CSS files
- [ ] Permissions set for JS files
- [ ] Permissions set for images
- [ ] Permissions set for PDF
- [ ] Permissions set for directories

---

## 🧪 TESTING CHECKLIST

### **Page Load Tests:**
- [ ] Homepage loads (http://yourdomain.com/)
- [ ] Available units page loads
- [ ] Unit 720C page loads
- [ ] Unit 730A page loads
- [ ] Unit 151A page loads
- [ ] Floor plans page loads
- [ ] Amenities page loads
- [ ] Gallery page loads
- [ ] Neighborhood page loads
- [ ] Contact page loads
- [ ] Rental application page loads

### **Image Tests:**
- [ ] Homepage images display
- [ ] Unit 720C images display (13 photos)
- [ ] Unit 730A images display (5 photos)
- [ ] Unit 151A images display
- [ ] Gallery images display
- [ ] Neighborhood images display (6 photos)

### **Functionality Tests:**
- [ ] Navigation menu works
- [ ] All links work
- [ ] Mobile menu works
- [ ] PDF downloads (rental application)
- [ ] Contact form displays
- [ ] Rental application form displays

### **Browser Console Tests:**
- [ ] No 404 errors in console
- [ ] No image loading errors
- [ ] No JavaScript errors
- [ ] No CSS loading errors

### **Mobile Tests:**
- [ ] Site displays correctly on mobile
- [ ] Navigation works on mobile
- [ ] Images load on mobile
- [ ] Forms work on mobile

---

## 🐛 TROUBLESHOOTING CHECKLIST

If something doesn't work:

### **Images Not Loading?**
- [ ] Check file exists: `ls -la images/filename.jpg`
- [ ] Check permissions: should be 644
- [ ] Check case: filename in HTML must match exactly
- [ ] Run: `chmod 644 images/*.jpg`

### **Permission Errors?**
- [ ] Check file ownership: `ls -la`
- [ ] Should be owned by www-data or apache
- [ ] Run: `sudo chown -R www-data:www-data /var/www/html`
- [ ] Recheck permissions: 644 for files, 755 for directories

### **404 Errors?**
- [ ] Check file exists on server
- [ ] Check filename case matches HTML reference
- [ ] Check web root is correct
- [ ] Check Apache/Nginx is running

### **Still Having Issues?**
- [ ] Check server logs: `/var/log/apache2/error.log`
- [ ] Test with curl: `curl http://yourdomain.com/ -I`
- [ ] Verify DNS is pointing to correct server
- [ ] Check firewall allows HTTP/HTTPS

---

## ✅ SUCCESS CRITERIA

Your site is successfully deployed when:

- [ ] All pages load without errors
- [ ] All images display correctly
- [ ] Navigation works smoothly
- [ ] Forms are functional
- [ ] PDF downloads work
- [ ] Mobile view looks good
- [ ] No console errors
- [ ] All unit pages work
- [ ] Gallery loads correctly
- [ ] Contact info displays

---

## 📊 QUICK STATS

- **Total HTML files**: 12
- **Total images**: 50+
- **Total file references checked**: 56
- **Broken links found**: 0
- **Case issues found**: 0 (all fixed)
- **Files with wrong permissions**: 0 (all fixed)

---

## 🎉 READY TO GO!

All pre-deployment tasks are complete. Your website is ready for Linux hosting!

**Next step**: Upload files to your server and follow the post-upload checklist above.

---

For detailed instructions, see:
- `LINUX_DEPLOYMENT_GUIDE.md` - Complete deployment guide
- `quick-reference.sh` - Quick command reference
- `LINUX_COMPATIBILITY_REPORT.md` - Detailed report
