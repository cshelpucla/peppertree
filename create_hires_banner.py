from PIL import Image, ImageOps
import os

def create_hires_banner(source_path, output_path, banner_width_ft, banner_height_ft, dpi):
    """
    Upscales an image to a high resolution suitable for a large format banner.

    Args:
        source_path (str): Path to the source image.
        output_path (str): Path to save the high-resolution image.
        banner_width_ft (int): The width of the physical banner in feet.
        banner_height_ft (int): The height of the physical banner in feet.
        dpi (int): The desired dots per inch for printing.
    """
    print("--- High-Resolution Banner Creator ---")
    
    # 1. Calculate target pixel dimensions
    target_width_px = int(banner_width_ft * 12 * dpi)
    target_height_px = int(banner_height_ft * 12 * dpi)
    target_aspect_ratio = target_width_px / target_height_px
    
    print(f"Target Dimensions: {target_width_px}px x {target_height_px}px at {dpi} DPI")
    print(f"Target Aspect Ratio: {target_aspect_ratio:.2f}")

    # 2. Open the source image
    try:
        source_image = Image.open(source_path)
        print(f"Successfully opened source image: {source_path}")
        print(f"Original Dimensions: {source_image.width}px x {source_image.height}px")
    except FileNotFoundError:
        print(f"ERROR: Source file not found at '{source_path}'. Aborting.")
        return
    except Exception as e:
        print(f"ERROR: Could not open source image. {e}")
        return

    # 3. Crop the image to the target aspect ratio before resizing
    # This prevents the image from being stretched or squished.
    print("Cropping image to match banner aspect ratio...")
    cropped_image = ImageOps.fit(source_image, 
                                 (int(source_image.width), int(source_image.width / target_aspect_ratio)), 
                                 method=Image.LANCZOS, 
                                 bleed=0.0, 
                                 centering=(0.5, 0.5))
    
    print(f"Cropped Dimensions: {cropped_image.width}px x {cropped_image.height}px")

    # 4. Resize the cropped image to the final high resolution
    print(f"Resizing image to {target_width_px} x {target_height_px}...")
    try:
        hires_image = cropped_image.resize((target_width_px, target_height_px), Image.LANCZOS)
        print("Image resized successfully.")
    except Exception as e:
        print(f"ERROR: Failed to resize image. {e}")
        return

    # 5. Save the new image
    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Save with high quality settings
        hires_image.save(output_path, format='PNG')
        print(f"SUCCESS: High-resolution banner saved to '{output_path}'")
    except Exception as e:
        print(f"ERROR: Failed to save the new image. {e}")

if __name__ == "__main__":
    # Configuration
    SOURCE_IMAGE = os.path.join("images", "IMG_3858.png")
    OUTPUT_IMAGE = os.path.join("images", "IMG_3858_banner_hires.png")
    BANNER_WIDTH_FEET = 8
    BANNER_HEIGHT_FEET = 4
    PRINT_DPI = 150 # 150 is a good balance for large banners viewed from a distance

    create_hires_banner(SOURCE_IMAGE, OUTPUT_IMAGE, BANNER_WIDTH_FEET, BANNER_HEIGHT_FEET, PRINT_DPI)
