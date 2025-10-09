from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

def create_for_rent_sign(output_path, banner_width_ft, banner_height_ft, dpi):
    """
    Designs and generates a high-resolution 'For Rent' sign for PepperTree Townhomes.
    """
    print("--- For Rent Sign Designer ---")

    # --- 1. Configuration ---
    background_image_path = os.path.join("images", "730_750_Outside2.jpg")
    
    # Colors from the website's CSS for high contrast
    primary_color = "#2c5f2d"
    secondary_color = "#97be5a"
    white_color = "#ffffff"
    accent_color = "#ffc857" # Yellow for specials

    # Text Content
    main_headline = "FOR RENT"
    property_name = "PepperTree Townhomes"
    phone_number = "(555) 555-5555"
    special_offer = "MOVE-IN SPECIAL!"
    unit_types = "Spacious 2 & 3 Bedroom Homes"

    # --- 2. Calculate Dimensions & Create Base ---
    target_width_px = int(banner_width_ft * 12 * dpi)
    target_height_px = int(banner_height_ft * 12 * dpi)
    target_aspect_ratio = target_width_px / target_height_px
    
    print(f"Target: {target_width_px}px x {target_height_px}px at {dpi} DPI")

    try:
        background = Image.open(background_image_path)
        print(f"Opened background: {background_image_path}")
    except FileNotFoundError:
        print(f"ERROR: Background image not found. Using a solid color.")
        background = Image.new("RGB", (target_width_px, target_height_px), primary_color)
    
    # Crop and resize background to fit the banner dimensions
    background = ImageOps.fit(background, (target_width_px, target_height_px), method=Image.LANCZOS)
    draw = ImageDraw.Draw(background, "RGBA")

    # --- 3. Add Overlays for Readability ---
    # Add a subtle darkening gradient to the whole image
    for i in range(target_height_px):
        alpha = int(50 + (i / target_height_px) * 100) # Gradient from ~20% to ~60% opacity
        draw.line([(0, i), (target_width_px, i)], fill=(0, 0, 0, alpha))

    # Add a solid bar at the bottom for the phone number
    bottom_bar_height = int(target_height_px * 0.25)
    draw.rectangle([(0, target_height_px - bottom_bar_height), (target_width_px, target_height_px)], fill=primary_color)

    # --- 4. Prepare Fonts ---
    try:
        # Using a bold, clear font like Arial Bold is best for signs
        font_path_bold = "arialbd.ttf"
        font_path_regular = "arial.ttf"
        font_headline = ImageFont.truetype(font_path_bold, int(target_height_px * 0.25))
        font_phone = ImageFont.truetype(font_path_bold, int(target_height_px * 0.15))
        font_special = ImageFont.truetype(font_path_bold, int(target_height_px * 0.1))
        font_details = ImageFont.truetype(font_path_regular, int(target_height_px * 0.06))
    except IOError:
        print("Arial font not found, using default.")
        # Fallback to default fonts with estimated sizes
        font_headline = ImageFont.load_default()
        font_phone = ImageFont.load_default()
        font_special = ImageFont.load_default()
        font_details = ImageFont.load_default()

    # --- 5. Draw Text Elements ---
    
    # Headline: "FOR RENT"
    headline_bbox = draw.textbbox((0, 0), main_headline, font=font_headline)
    headline_width = headline_bbox[2] - headline_bbox[0]
    draw.text(
        ((target_width_px - headline_width) / 2, int(target_height_px * 0.05)),
        main_headline,
        font=font_headline,
        fill=white_color,
        stroke_width=6,
        stroke_fill=(0,0,0,100) # Subtle drop shadow
    )

    # Property Name
    details_bbox = draw.textbbox((0, 0), property_name, font=font_details)
    details_width = details_bbox[2] - details_bbox[0]
    draw.text(
        ((target_width_px - details_width) / 2, int(target_height_px * 0.35)),
        property_name,
        font=font_details,
        fill=secondary_color
    )
    
    # Unit Types
    details_bbox = draw.textbbox((0, 0), unit_types, font=font_details)
    details_width = details_bbox[2] - details_bbox[0]
    draw.text(
        ((target_width_px - details_width) / 2, int(target_height_px * 0.45)),
        unit_types,
        font=font_details,
        fill=white_color
    )

    # Special Offer
    special_bbox = draw.textbbox((0, 0), special_offer, font=font_special)
    special_width = special_bbox[2] - special_bbox[0]
    draw.text(
        ((target_width_px - special_width) / 2, int(target_height_px * 0.58)),
        special_offer,
        font=font_special,
        fill=accent_color
    )

    # Phone Number
    phone_bbox = draw.textbbox((0, 0), phone_number, font=font_phone)
    phone_width = phone_bbox[2] - phone_bbox[0]
    phone_height = phone_bbox[3] - phone_bbox[1]
    draw.text(
        ((target_width_px - phone_width) / 2, target_height_px - bottom_bar_height / 2 - phone_height / 2),
        phone_number,
        font=font_phone,
        fill=white_color
    )

    # --- 6. Save the Final Image ---
    try:
        if background.mode == 'RGBA':
            background = background.convert('RGB')
        background.save(output_path, "JPEG", quality=95, dpi=(dpi, dpi))
        print(f"SUCCESS: 'For Rent' sign saved to '{output_path}'")
    except Exception as e:
        print(f"ERROR: Failed to save the image. {e}")

if __name__ == "__main__":
    create_for_rent_sign(
        output_path=os.path.join("images", "for_rent_sign_8x4.jpg"),
        banner_width_ft=8,
        banner_height_ft=4,
        dpi=150
    )
