from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import os
import numpy as np

def create_ultra_professional_sign(output_path, banner_width_ft, banner_height_ft, dpi):
    """
    Creates an ultra-professional, high-impact 'For Rent' sign with enhanced design elements.
    Features: Sophisticated color scheme, layered design, optimized typography, visual balance.
    """
    print("=== Ultra-Professional Sign Designer v3.0 ===")

    # --- 1. Professional Configuration ---
    target_width_px = int(banner_width_ft * 12 * dpi)
    target_height_px = int(banner_height_ft * 12 * dpi)
    
    # Sophisticated Color Palette (Real Estate Professional)
    deep_navy = "#1a2332"        # Primary brand color - sophisticated, trustworthy
    crisp_white = "#FFFFFF"       # Primary text color
    warm_gold = "#d4af37"         # Accent/highlight - premium feel
    soft_cream = "#f5f5f0"        # Secondary background
    dark_text = "#2c2c2c"         # Text on light backgrounds
    overlay_shadow = (0, 0, 0, 120)  # For photo overlays
    
    # Photo Path
    photo_path = os.path.join("images", "730_750_Outside2.jpg")

    # --- 2. Create the High-Resolution Canvas ---
    print("→ Creating high-resolution canvas (14400 x 7200 pixels)")
    img = Image.new("RGB", (target_width_px, target_height_px), soft_cream)
    draw = ImageDraw.Draw(img, "RGBA")

    # --- 3. Advanced Layout: Asymmetric Balance with Visual Weight ---
    # Left 55% for image, Right 45% for information - creates dynamic tension
    info_panel_start_x = int(target_width_px * 0.55)
    
    # Add a subtle gradient overlay to the right panel for depth
    info_panel_width = target_width_px - info_panel_start_x
    
    # Panel 1: Property Image with Vignette Effect
    try:
        property_photo = Image.open(photo_path)
        photo_panel_width = info_panel_start_x
        photo_panel_height = target_height_px
        
        # Perfect crop for the photo
        photo_cropped = ImageOps.fit(property_photo, (photo_panel_width, photo_panel_height), method=Image.LANCZOS)
        
        # Apply subtle vignette for professional look
        vignette = Image.new("RGBA", (photo_panel_width, photo_panel_height), (0, 0, 0, 0))
        vignette_draw = ImageDraw.Draw(vignette)
        for i in range(0, min(photo_panel_width, photo_panel_height) // 6):
            alpha = int(60 * (i / (min(photo_panel_width, photo_panel_height) // 6)))
            vignette_draw.rectangle(
                [(i, i), (photo_panel_width - i, photo_panel_height - i)],
                outline=(0, 0, 0, alpha)
            )
        
        img.paste(photo_cropped, (0, 0))
        img.paste(vignette, (0, 0), vignette)
        print("→ Placed property image with professional vignette")
    except FileNotFoundError:
        print(f"⚠ Warning: Photo not found at {photo_path}. Using placeholder.")
        draw.rectangle([(0, 0), (info_panel_start_x, target_height_px)], fill="#c0c0c0")

    # Panel 2: Information Panel with Depth
    # Create a subtle gradient effect on the info panel
    draw.rectangle([(info_panel_start_x, 0), (target_width_px, target_height_px)], fill=deep_navy)
    
    # Add a thin accent line separator
    separator_width = int(target_width_px * 0.008)
    draw.rectangle(
        [(info_panel_start_x - separator_width, 0), (info_panel_start_x, target_height_px)],
        fill=warm_gold
    )
    print("→ Created information panel with accent separator")

    # --- 4. Premium Typography System ---
    try:
        # Use multiple font weights for hierarchy
        font_path_bold = "arialbd.ttf"
        font_path_regular = "arial.ttf"
        
        # Optimized font sizes for readability at distance
        font_mega = ImageFont.truetype(font_path_bold, int(target_height_px * 0.20))      # FOR RENT
        font_huge = ImageFont.truetype(font_path_bold, int(target_height_px * 0.13))      # Phone
        font_large = ImageFont.truetype(font_path_bold, int(target_height_px * 0.075))    # Details
        font_medium = ImageFont.truetype(font_path_regular, int(target_height_px * 0.055)) # Secondary
        font_small = ImageFont.truetype(font_path_regular, int(target_height_px * 0.04))   # Fine print
    except IOError:
        print("⚠ Using default fonts")
        font_mega = font_huge = font_large = font_medium = font_small = ImageFont.load_default()

    # --- 5. Strategic Content Placement with Visual Hierarchy ---
    info_panel_center_x = info_panel_start_x + info_panel_width / 2
    margin_x = int(info_panel_width * 0.08)  # Side margins within info panel
    
    # Top Section: PRIMARY MESSAGE
    y_position = int(target_height_px * 0.08)
    
    # "FOR RENT" - Maximum Impact
    rent_text = "FOR RENT"
    rent_bbox = draw.textbbox((0, 0), rent_text, font=font_mega)
    rent_width = rent_bbox[2] - rent_bbox[0]
    rent_height = rent_bbox[3] - rent_bbox[1]
    
    # Add subtle shadow for depth
    shadow_offset = 8
    draw.text(
        (info_panel_center_x - rent_width / 2 + shadow_offset, y_position + shadow_offset),
        rent_text, font=font_mega, fill=(0, 0, 0, 80)
    )
    draw.text(
        (info_panel_center_x - rent_width / 2, y_position),
        rent_text, font=font_mega, fill=crisp_white
    )
    
    y_position += rent_height + int(target_height_px * 0.04)
    
    # Decorative underline
    underline_width = int(rent_width * 0.6)
    draw.rectangle(
        [(info_panel_center_x - underline_width / 2, y_position),
         (info_panel_center_x + underline_width / 2, y_position + int(target_height_px * 0.008))],
        fill=warm_gold
    )
    
    print("→ Placed primary headline with shadow and accent")
    
    # Middle Section: PREMIUM OFFER BOX
    y_position += int(target_height_px * 0.08)
    
    # Create a premium offer box
    box_height = int(target_height_px * 0.20)
    box_padding = int(target_height_px * 0.03)
    box_y_start = y_position
    
    draw.rounded_rectangle(
        [(info_panel_start_x + margin_x, box_y_start),
         (target_width_px - margin_x, box_y_start + box_height)],
        radius=20, fill=warm_gold
    )
    
    # Special offer text
    special_main = "3 BED / 2.5 BATH"
    special_sub = "MOVE-IN SPECIALS AVAILABLE"
    
    special_bbox = draw.textbbox((0, 0), special_main, font=font_large)
    special_width = special_bbox[2] - special_bbox[0]
    special_height = special_bbox[3] - special_bbox[1]
    
    draw.text(
        (info_panel_center_x - special_width / 2, box_y_start + box_padding),
        special_main, font=font_large, fill=dark_text
    )
    
    sub_bbox = draw.textbbox((0, 0), special_sub, font=font_medium)
    sub_width = sub_bbox[2] - sub_bbox[0]
    
    draw.text(
        (info_panel_center_x - sub_width / 2, box_y_start + box_padding + special_height + int(target_height_px * 0.02)),
        special_sub, font=font_medium, fill=dark_text
    )
    
    print("→ Created premium offer box with unit details")
    
    # Bottom Section: CALL TO ACTION
    y_position = box_y_start + box_height + int(target_height_px * 0.08)
    
    # "CALL TODAY" label
    call_label = "CALL TODAY"
    call_label_bbox = draw.textbbox((0, 0), call_label, font=font_medium)
    call_label_width = call_label_bbox[2] - call_label_bbox[0]
    
    draw.text(
        (info_panel_center_x - call_label_width / 2, y_position),
        call_label, font=font_medium, fill=warm_gold
    )
    
    y_position += call_label_bbox[3] + int(target_height_px * 0.02)
    
    # Phone Number - High Contrast, Maximum Visibility
    phone_text = "(559) 935-2985"
    phone_bbox = draw.textbbox((0, 0), phone_text, font=font_huge)
    phone_width = phone_bbox[2] - phone_bbox[0]
    
    # Add background box for phone number
    phone_box_padding = int(target_height_px * 0.02)
    draw.rounded_rectangle(
        [(info_panel_center_x - phone_width / 2 - phone_box_padding, y_position - phone_box_padding),
         (info_panel_center_x + phone_width / 2 + phone_box_padding, y_position + phone_bbox[3] + phone_box_padding)],
        radius=15, fill=(255, 255, 255, 30)
    )
    
    draw.text(
        (info_panel_center_x - phone_width / 2, y_position),
        phone_text, font=font_huge, fill=crisp_white
    )
    
    print("→ Placed call-to-action with enhanced visibility")
    
    # --- 6. Branding & Professional Details ---
    
    # Top branding on photo with premium badge design
    brand_text = "PEPPER TREE TOWNHOMES"
    brand_bbox = draw.textbbox((0, 0), brand_text, font=font_medium)
    brand_width = brand_bbox[2] - brand_bbox[0]
    brand_height = brand_bbox[3] - brand_bbox[1]
    
    # Create a premium badge shape
    badge_x = int(target_width_px * 0.05)
    badge_y = int(target_height_px * 0.06)
    badge_padding_x = int(target_width_px * 0.03)
    badge_padding_y = int(target_height_px * 0.02)
    
    draw.rounded_rectangle(
        [(badge_x - badge_padding_x, badge_y - badge_padding_y),
         (badge_x + brand_width + badge_padding_x, badge_y + brand_height + badge_padding_y)],
        radius=10, fill=overlay_shadow
    )
    draw.rounded_rectangle(
        [(badge_x - badge_padding_x + 4, badge_y - badge_padding_y + 4),
         (badge_x + brand_width + badge_padding_x - 4, badge_y + brand_height + badge_padding_y - 4)],
        radius=8, fill=deep_navy
    )
    
    draw.text((badge_x, badge_y), brand_text, font=font_medium, fill=warm_gold)
    
    print("→ Added premium branding badge")
    
    # Bottom footer with additional info
    footer_y = int(target_height_px * 0.93)
    footer_text = "PROFESSIONALLY MANAGED • AVAILABLE NOW"
    footer_bbox = draw.textbbox((0, 0), footer_text, font=font_small)
    footer_width = footer_bbox[2] - footer_bbox[0]
    
    draw.text(
        (info_panel_center_x - footer_width / 2, footer_y),
        footer_text, font=font_small, fill=(255, 255, 255, 180)
    )
    
    # --- 7. Final Polish & Export ---
    print("→ Applying final enhancements...")
    
    # Save with maximum quality
    try:
        img.save(output_path, "JPEG", quality=98, dpi=(dpi, dpi), optimize=True)
        print(f"✓ SUCCESS: Ultra-professional sign saved to '{output_path}'")
        print(f"  Dimensions: {target_width_px} x {target_height_px} pixels")
        print(f"  Physical Size: {banner_width_ft}' x {banner_height_ft}' @ {dpi} DPI")
    except Exception as e:
        print(f"✗ ERROR: Failed to save image. {e}")

if __name__ == "__main__":
    create_ultra_professional_sign(
        output_path=os.path.join("images", "for_rent_sign_professional_v3_8x4.jpg"),
        banner_width_ft=8,
        banner_height_ft=4,
        dpi=150
    )
