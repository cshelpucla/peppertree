"""
Convert HEIC images to JPEG format and move originals to archive
"""
import os
from pathlib import Path

try:
    from PIL import Image
    import pillow_heif
    pillow_heif.register_heif_opener()
    HAS_HEIF = True
except ImportError:
    HAS_HEIF = False
    print("pillow-heif not installed. Attempting to install...")

def install_dependencies():
    """Install required packages"""
    import subprocess
    try:
        subprocess.check_call(['pip', 'install', 'pillow-heif', 'pillow'])
        print("Successfully installed pillow-heif")
        return True
    except:
        print("Failed to install pillow-heif")
        return False

def convert_heic_to_jpeg(images_dir='images', archive_dir='images/ImgArch'):
    """Convert all HEIC files to JPEG and move originals"""
    if not HAS_HEIF:
        if install_dependencies():
            # Re-import after installation
            from PIL import Image
            import pillow_heif
            pillow_heif.register_heif_opener()
        else:
            print("Cannot proceed without pillow-heif")
            return
    
    from PIL import Image
    import pillow_heif
    
    images_path = Path(images_dir)
    archive_path = Path(archive_dir)
    
    # Ensure archive directory exists
    archive_path.mkdir(parents=True, exist_ok=True)
    
    # Find all HEIC files
    heic_files = list(images_path.glob('*.HEIC')) + list(images_path.glob('*.heic'))
    
    if not heic_files:
        print("No HEIC files found in images directory")
        return
    
    print(f"Found {len(heic_files)} HEIC files to convert")
    
    converted = 0
    failed = 0
    
    for heic_file in heic_files:
        try:
            # Read HEIC file using pillow_heif
            heif_file = pillow_heif.read_heif(str(heic_file))
            
            # Convert to PIL Image
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )
            
            # Convert to RGB if necessary
            if image.mode in ('RGBA', 'LA', 'P'):
                image = image.convert('RGB')
            
            # Create output filename
            output_name = heic_file.stem + '.jpg'
            output_path = images_path / output_name
            
            # Save as JPEG
            image.save(output_path, 'JPEG', quality=95)
            image.close()
            
            # Move original to archive
            archive_file = archive_path / heic_file.name
            heic_file.rename(archive_file)
            
            print(f"✓ Converted: {heic_file.name} -> {output_name}")
            converted += 1
            
        except Exception as e:
            print(f"✗ Failed to convert {heic_file.name}: {str(e)}")
            failed += 1
    
    print(f"\nConversion complete!")
    print(f"Successfully converted: {converted} files")
    print(f"Failed: {failed} files")
    print(f"Originals moved to: {archive_path}")

if __name__ == '__main__':
    convert_heic_to_jpeg()
