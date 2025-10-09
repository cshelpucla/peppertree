from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

def create_expert_sign_v2(output_path, banner_width_ft, banner_height_ft, dpi):
    """
    Designs and generates a professional, high-impact 'For Rent' sign from scratch.
    This design prioritizes clarity, readability, and modern aesthetics.
    """
    print("--- Expert Sign Designer v2.0 (From Scratch) ---")

    # --- 1. Professional Configuration ---
    target_width_px = int(banner_width_ft * 12 * dpi)
    target_height_px = int(banner_height_ft * 12 * dpi)
    
    # High-Contrast & Professional Color Palette
    brand_green_dark = "#2c5f2d"
    brand_white = "#FFFFFF"
    brand_accent_gold = "#ffc857"
    text_dark = "#1a1a1a"

    # Photo Path
    photo_path = os.path.join("images", "730_750_Outside2.jpg")

    # --- 2. Create the High-Resolution Canvas ---
    print("Creating high-resolution canvas.")
    img = Image.new("RGB", (target_width_px, target_height_px), brand_white)
    draw = ImageDraw.Draw(img, "RGBA")

    # --- 3. Two-Panel Layout: Image and Color Block ---
    # The left 2/3 will be the image, the right 1/3 will be the info block.
    info_panel_start_x = int(target_width_px * 0.6)

    # Panel 1: The Property Image
    try:
        property_photo = Image.open(photo_path)
        # Crop the photo to fit the panel dimensions perfectly
        photo_panel_width = info_panel_start_x
        photo_panel_height = target_height_px
        photo_cropped = ImageOps.fit(property_photo, (photo_panel_width, photo_panel_height), method=Image.LANCZOS)
        img.paste(photo_cropped, (0, 0))
        print("Placed high-quality, cropped property image.")
    except FileNotFoundError:
        print(f"Warning: Photo not found at {photo_path}. Using a placeholder.")
        draw.rectangle([(0, 0), (info_panel_start_x, target_height_px)], fill="#e0e0e0")

    # Panel 2: The Information Color Block
    draw.rectangle([(info_panel_start_x, 0), (target_width_px, target_height_px)], fill=brand_green_dark)
    print("Created high-contrast information panel.")

    # --- 4. Expert Typography: Clean, Bold, Legible ---
    try:
        # A clean, bold, sans-serif font is best for distance readability.
        font_path = "arialbd.ttf"
        font_huge = ImageFont.truetype(font_path, int(target_height_px * 0.22))
        font_large = ImageFont.truetype(font_path, int(target_height_px * 0.14))
        font_medium = ImageFont.truetype(font_path, int(target_height_px * 0.06))
    except IOError:
        print("Using default fonts.")
        font_huge, font_large, font_medium = (ImageFont.load_default(),)*3

    # --- 5. Place Text with Clear Hierarchy ---
    info_panel_center_x = info_panel_start_x + (target_width_px - info_panel_start_x) / 2
    
    # "FOR RENT" - The Primary Message
    rent_bbox = draw.textbbox((0, 0), "FOR RENT", font=font_huge)
    rent_width = rent_bbox[2] - rent_bbox[0]
    draw.text(
        (info_panel_center_x - rent_width / 2, int(target_height_px * 0.1)),
        "FOR RENT", font=font_huge, fill=brand_white
    )

    # Phone Number - The Primary Call to Action
    phone_bbox = draw.textbbox((0, 0), "(559) 935-2985", font=font_large)
    phone_width = phone_bbox[2] - phone_bbox[0]
    draw.text(
        (info_panel_center_x - phone_width / 2, int(target_height_px * 0.75)),
        "(559) 935-2985", font=font_large, fill=brand_white
    )
    print("Placed primary text elements with maximum legibility.")

    # --- 6. Add Branding and Secondary Information ---
    
    # Property Name (on the photo for context)
    brand_text = "PepperTree Townhomes"
    brand_bbox = draw.textbbox((0,0), brand_text, font=font_medium)
    brand_width = brand_bbox[2] - brand_bbox[0]
    brand_pos = (int(target_width_px * 0.03), int(target_height_px * 0.03))
    # Add a semi-transparent background for the text on the image
    draw.rectangle(
        (brand_pos[0] - 20, brand_pos[1] - 20, brand_pos[0] + brand_width + 20, brand_pos[1] + brand_bbox[3] + 20),
        fill=(0,0,0,100)
    )
    draw.text(brand_pos, brand_text, font=font_medium, fill=brand_white)
    print("Placed branding text.")

    # "Move-In Special" - The Incentive
    special_text = "MOVE-IN SPECIAL!"
    special_bbox = draw.textbbox((0,0), special_text, font=font_medium)
    special_width = special_bbox[2] - special_bbox[0]
    
    # Create a gold banner element for the special
    banner_height = int(target_height_px * 0.12)
    draw.rectangle(
        [(info_panel_start_x, int(target_height_px * 0.45)), (target_width_px, int(target_height_px * 0.45) + banner_height)],
        fill=brand_accent_gold
    )
    draw.text(
        (info_panel_center_x - special_width / 2, int(target_height_px * 0.45) + (banner_height - special_bbox[3])/2),
        special_text, font=font_medium, fill=text_dark
    )
    print("Added incentive banner.")

    # --- 7. Save the Final Product ---
    try:
        img.save(output_path, "JPEG", quality=95, dpi=(dpi, dpi))
        print(f"SUCCESS: A new, professionally designed sign has been saved to '{output_path}'")
    except Exception as e:
        print(f"ERROR: Failed to save the image. {e}")

if __name__ == "__main__":
    create_expert_sign_v2(
        output_path=os.path.join("images", "for_rent_sign_expert_v2_8x4.jpg"),
        banner_width_ft=8,
        banner_height_ft=4,
        dpi=150
    )
