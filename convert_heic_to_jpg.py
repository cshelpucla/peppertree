"""
Convert HEIC images to JPEG and move originals to archive
"""
import os
import shutil
from pathlib import Path
from PIL import Image
import pillow_heif

# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()

def convert_heic_to_jpg(images_dir="images", archive_dir="images/ImgArch"):
    """
    Convert all HEIC files in images directory to JPEG
    Move original HEIC files to archive directory
    """
    images_path = Path(images_dir)
    archive_path = Path(archive_dir)
    
    # Create archive directory if it doesn't exist
    archive_path.mkdir(parents=True, exist_ok=True)
    
    # Find all HEIC files in images directory (not in subdirectories)
    heic_files = list(images_path.glob("*.HEIC")) + list(images_path.glob("*.heic"))
    
    if not heic_files:
        print(f"No HEIC files found in {images_dir}")
        return
    
    print(f"Found {len(heic_files)} HEIC files to convert")
    print("-" * 60)
    
    converted_count = 0
    error_count = 0
    
    for heic_file in heic_files:
        # Skip if file is already in archive directory
        if archive_dir in str(heic_file):
            continue
            
        try:
            # Create output JPEG filename
            jpg_filename = heic_file.stem + ".jpg"
            jpg_path = images_path / jpg_filename
            
            print(f"Converting: {heic_file.name}")
            
            # Open and convert HEIC to JPEG
            image = Image.open(heic_file)
            
            # Convert to RGB if necessary (HEIC might have RGBA)
            if image.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', image.size, (255, 255, 255))
                if image.mode == 'P':
                    image = image.convert('RGBA')
                background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                image = background
            elif image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Save as JPEG with high quality
            image.save(jpg_path, 'JPEG', quality=95, optimize=True)
            
            print(f"  → Saved as: {jpg_filename}")
            
            # Move original HEIC to archive
            archive_file = archive_path / heic_file.name
            
            # If file already exists in archive, add number suffix
            if archive_file.exists():
                counter = 1
                while archive_file.exists():
                    archive_file = archive_path / f"{heic_file.stem}_{counter}.HEIC"
                    counter += 1
            
            shutil.move(str(heic_file), str(archive_file))
            print(f"  → Moved original to: {archive_file.relative_to(images_path)}")
            
            converted_count += 1
            
        except Exception as e:
            print(f"  ✗ Error converting {heic_file.name}: {e}")
            error_count += 1
        
        print()
    
    print("-" * 60)
    print(f"Conversion complete!")
    print(f"  ✓ Converted: {converted_count} files")
    if error_count > 0:
        print(f"  ✗ Errors: {error_count} files")
    print(f"  📁 Originals archived in: {archive_dir}")

if __name__ == "__main__":
    print("=" * 60)
    print("HEIC to JPEG Converter")
    print("=" * 60)
    print()
    
    convert_heic_to_jpg()
    
    print()
    print("Done!")
