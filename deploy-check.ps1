# PepperTree Website Deployment Script
# This script prepares the website for hosting by setting proper permissions and validating structure

Write-Host "🏠 PepperTree Website Deployment Preparation" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green

# Set working directory
$websiteRoot = "c:\Users\arovi\vscode\peppertree"
Set-Location $websiteRoot

Write-Host "`n📁 Checking file structure..." -ForegroundColor Yellow

# Core files that must exist
$coreFiles = @(
    "index.html",
    "rental-application.html", 
    "rental-application-form.html",
    "available.html",
    "contact.html",
    "gallery.html",
    "neighborhood.html",
    "amenities.html",
    "floorplans.html",
    "styles.css",
    "script.js",
    "Golden_Hills_Rental_Application_Fillable.pdf"
)

$missingFiles = @()
foreach ($file in $coreFiles) {
    if (Test-Path $file) {
        Write-Host "  ✅ $file" -ForegroundColor Green
    } else {
        Write-Host "  ❌ $file" -ForegroundColor Red
        $missingFiles += $file
    }
}

Write-Host "`n🖼️ Checking images directory..." -ForegroundColor Yellow

if (Test-Path "images") {
    $imageCount = (Get-ChildItem "images" -File).Count
    Write-Host "  ✅ Images directory exists with $imageCount files" -ForegroundColor Green
    
    # Check for essential images
    $essentialImages = @(
        "unit-1-exterior.jpg",
        "unit-2-living.jpg", 
        "unit-3-kitchen.jpg",
        "720C_LivingRoom.jpg",
        "730_750_Outside.jpg",
        "131_Outside_Bldg.jpg"
    )
    
    foreach ($img in $essentialImages) {
        if (Test-Path "images\$img") {
            Write-Host "  ✅ Essential image: $img" -ForegroundColor Green
        } else {
            Write-Host "  ⚠️ Missing essential image: $img" -ForegroundColor Yellow
        }
    }
} else {
    Write-Host "  ❌ Images directory missing!" -ForegroundColor Red
    $missingFiles += "images/"
}

Write-Host "`n🔗 Validating image references..." -ForegroundColor Yellow

# Simple check for broken image references in HTML files
$htmlFiles = Get-ChildItem "*.html" -File
$brokenReferences = @()

foreach ($htmlFile in $htmlFiles) {
    $content = Get-Content $htmlFile.FullName -Raw
    $imageMatches = [regex]::Matches($content, 'src=["\']images/([^"\']+)["\']')
    
    foreach ($match in $imageMatches) {
        $imagePath = $match.Groups[1].Value
        $fullPath = "images\$imagePath"
        
        if (-not (Test-Path $fullPath)) {
            $brokenReferences += "$($htmlFile.Name): images/$imagePath"
        }
    }
}

if ($brokenReferences.Count -eq 0) {
    Write-Host "  ✅ All image references are valid" -ForegroundColor Green
} else {
    Write-Host "  ⚠️ Found broken image references:" -ForegroundColor Yellow
    foreach ($ref in $brokenReferences) {
        Write-Host "    - $ref" -ForegroundColor Red
    }
}

Write-Host "`n📊 Deployment Readiness Summary" -ForegroundColor Cyan
Write-Host "===============================" -ForegroundColor Cyan

if ($missingFiles.Count -eq 0 -and $brokenReferences.Count -eq 0) {
    Write-Host "🎉 READY FOR HOSTING!" -ForegroundColor Green
    Write-Host "✅ All core files present" -ForegroundColor Green
    Write-Host "✅ All image references valid" -ForegroundColor Green
    Write-Host "✅ Proper file structure maintained" -ForegroundColor Green
    
    Write-Host "`n📋 Upload Instructions:" -ForegroundColor Yellow
    Write-Host "1. Upload all HTML files to web root" -ForegroundColor White
    Write-Host "2. Upload styles.css and script.js to web root" -ForegroundColor White
    Write-Host "3. Upload PDF file to web root" -ForegroundColor White
    Write-Host "4. Upload entire 'images' folder to web root" -ForegroundColor White
    Write-Host "5. Set file permissions to 644 for files, 755 for directories" -ForegroundColor White
    
} else {
    Write-Host "⚠️ ISSUES FOUND - Fix before hosting:" -ForegroundColor Red
    
    if ($missingFiles.Count -gt 0) {
        Write-Host "Missing files:" -ForegroundColor Red
        foreach ($file in $missingFiles) {
            Write-Host "  - $file" -ForegroundColor Red
        }
    }
    
    if ($brokenReferences.Count -gt 0) {
        Write-Host "Broken image references:" -ForegroundColor Red
        foreach ($ref in $brokenReferences) {
            Write-Host "  - $ref" -ForegroundColor Red
        }
    }
}

Write-Host "`n🌐 Test your website locally at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "📝 Check image-validator.html for detailed image validation" -ForegroundColor Cyan
