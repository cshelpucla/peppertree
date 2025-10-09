# Linux Hosting Preparation for PepperTree Website
# This creates a comprehensive report and fixes for Linux hosting

Write-Host "🐧 Linux Hosting Preparation for PepperTree Website" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green

# Set working directory
$websiteRoot = "c:\Users\arovi\vscode\peppertree"
Set-Location $websiteRoot

Write-Host "`n🔍 Analyzing Linux compatibility issues..." -ForegroundColor Yellow

# Check for case sensitivity issues
Write-Host "`n📁 Case Sensitivity Issues:" -ForegroundColor Cyan

$caseIssues = @()
$imageFiles = Get-ChildItem "images" -File

foreach ($file in $imageFiles) {
    if ($file.Name -cmatch '[A-Z]') {
        $caseIssues += $file.Name
        Write-Host "  ⚠️ $($file.Name) - Contains uppercase characters" -ForegroundColor Yellow
    }
}

Write-Host "`n🔗 Checking HTML references for case mismatches..." -ForegroundColor Cyan

$htmlFiles = Get-ChildItem "*.html" -File
$caseMismatches = @()

foreach ($htmlFile in $htmlFiles) {
    $content = Get-Content $htmlFile.FullName -Raw
    $imageMatches = [regex]::Matches($content, 'src=["\']images/([^"\']+)["\']')
    
    foreach ($match in $imageMatches) {
        $referencedImage = $match.Groups[1].Value
        $actualFile = Get-ChildItem "images" -File | Where-Object { $_.Name -ieq $referencedImage }
        
        if ($actualFile -and $actualFile.Name -cne $referencedImage) {
            $caseMismatches += @{
                File = $htmlFile.Name
                Referenced = $referencedImage
                Actual = $actualFile.Name
            }
            Write-Host "  ⚠️ $($htmlFile.Name): references '$referencedImage' but file is '$($actualFile.Name)'" -ForegroundColor Red
        }
    }
}

Write-Host "`n📊 Linux Compatibility Summary:" -ForegroundColor Cyan
Write-Host "Files with case issues: $($caseIssues.Count)" -ForegroundColor $(if($caseIssues.Count -eq 0) { 'Green' } else { 'Yellow' })
Write-Host "Case mismatches in HTML: $($caseMismatches.Count)" -ForegroundColor $(if($caseMismatches.Count -eq 0) { 'Green' } else { 'Red' })

if ($caseIssues.Count -gt 0 -or $caseMismatches.Count -gt 0) {
    Write-Host "`n⚠️ LINUX COMPATIBILITY ISSUES FOUND!" -ForegroundColor Red
    Write-Host "Linux is case-sensitive and these issues will cause broken images." -ForegroundColor Red
} else {
    Write-Host "`n✅ NO LINUX COMPATIBILITY ISSUES!" -ForegroundColor Green
}

Write-Host "`n📋 Recommended File Permission Commands for Linux:" -ForegroundColor Yellow
Write-Host "chmod 644 *.html *.css *.js *.pdf" -ForegroundColor White
Write-Host "chmod 644 images/*" -ForegroundColor White
Write-Host "chmod 755 images/" -ForegroundColor White
Write-Host "find . -type f -name '*.html' -exec chmod 644 {} \;" -ForegroundColor White
Write-Host "find . -type f -name '*.jpg' -exec chmod 644 {} \;" -ForegroundColor White
Write-Host "find . -type f -name '*.png' -exec chmod 644 {} \;" -ForegroundColor White
