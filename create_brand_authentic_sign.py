from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

def create_brand_authentic_sign(output_path, banner_width_ft, banner_height_ft, dpi):
    """
    Creates a 'For Rent' sign that authentically matches the Pepper Tree brand identity.
    Based on actual signage: green/cream color scheme, traditional typography, tree icon.
    """
    print("=== Pepper Tree Brand-Authentic Sign Designer ===")

    # --- 1. Authentic Brand Configuration ---
    target_width_px = int(banner_width_ft * 12 * dpi)
    target_height_px = int(banner_height_ft * 12 * dpi)
    
    # EXACT Brand Colors from Reference Signs
    pepper_green = "#1e5a3c"      # The signature deep green
    cream_background = "#f4efd3"  # Warm cream/beige background
    dark_brown = "#3d2817"        # Brown accent (from borders)
    white = "#FFFFFF"
    text_shadow = (0, 0, 0, 60)
    
    print(f"→ Creating {banner_width_ft}x{banner_height_ft}ft sign at {dpi} DPI")
    print(f"  Canvas: {target_width_px} x {target_height_px} pixels")

    # --- 2. Create Canvas with Brand Background ---
    img = Image.new("RGB", (target_width_px, target_height_px), cream_background)
    draw = ImageDraw.Draw(img, "RGBA")

    # Add elegant border (like reference signs)
    border_width = int(target_width_px * 0.015)
    draw.rectangle(
        [(0, 0), (target_width_px, target_height_px)],
        outline=dark_brown, width=border_width
    )
    
    # Inner decorative border
    inner_border_margin = int(target_width_px * 0.025)
    draw.rectangle(
        [(inner_border_margin, inner_border_margin), 
         (target_width_px - inner_border_margin, target_height_px - inner_border_margin)],
        outline=pepper_green, width=int(border_width * 0.6)
    )
    
    print("→ Applied brand-authentic borders and background")

    # --- 3. Load Fonts (Matching Brand Typography) ---
    try:
        # Traditional serif for "Pepper Tree" (like the script in references)
        font_path_serif = "georgia.ttf"  # Elegant serif
        font_path_bold = "arialbd.ttf"   # Bold for emphasis
        font_path_regular = "arial.ttf"  # Clean sans-serif
        
        # Font hierarchy matching brand style
        font_brand_huge = ImageFont.truetype(font_path_serif, int(target_height_px * 0.18))   # "Pepper Tree"
        font_headline = ImageFont.truetype(font_path_bold, int(target_height_px * 0.15))      # "FOR RENT"
        font_large = ImageFont.truetype(font_path_bold, int(target_height_px * 0.11))         # Phone
        font_medium = ImageFont.truetype(font_path_regular, int(target_height_px * 0.065))    # Details
        font_small = ImageFont.truetype(font_path_regular, int(target_height_px * 0.045))     # Fine print
    except IOError:
        print("⚠ Warning: Using default fonts")
        font_brand_huge = font_headline = font_large = font_medium = font_small = ImageFont.load_default()

    # --- 4. Draw Simple Tree Icon (Brand Symbol) ---
    # Center-top placement for tree icon
    tree_center_x = target_width_px // 2
    tree_top_y = int(target_height_px * 0.08)
    tree_size = int(target_height_px * 0.20)
    
    # Draw a simple, stylized tree silhouette
    # Tree canopy (circle/organic shape)
    canopy_radius = int(tree_size * 0.45)
    canopy_y = tree_top_y + canopy_radius
    
    # Three overlapping circles for fuller canopy
    for offset_x in [-canopy_radius//3, 0, canopy_radius//3]:
        draw.ellipse(
            [(tree_center_x + offset_x - canopy_radius, canopy_y - canopy_radius),
             (tree_center_x + offset_x + canopy_radius, canopy_y + canopy_radius)],
            fill=pepper_green
        )
    
    # Tree trunk
    trunk_width = int(tree_size * 0.12)
    trunk_height = int(tree_size * 0.35)
    trunk_x_left = tree_center_x - trunk_width // 2
    trunk_y_top = canopy_y + canopy_radius - int(trunk_height * 0.3)
    
    draw.rectangle(
        [(trunk_x_left, trunk_y_top),
         (trunk_x_left + trunk_width, trunk_y_top + trunk_height)],
        fill=dark_brown
    )
    
    print("→ Drew brand tree icon")

    # --- 5. Brand Name: "Pepper Tree" (Traditional Style) ---
    y_position = tree_top_y + tree_size + int(target_height_px * 0.03)
    
    brand_name = "Peppertree"
    brand_bbox = draw.textbbox((0, 0), brand_name, font=font_brand_huge)
    brand_width = brand_bbox[2] - brand_bbox[0]
    
    # Subtle shadow for depth
    shadow_offset = 6
    draw.text(
        (tree_center_x - brand_width / 2 + shadow_offset, y_position + shadow_offset),
        brand_name, font=font_brand_huge, fill=text_shadow
    )
    draw.text(
        (tree_center_x - brand_width / 2, y_position),
        brand_name, font=font_brand_huge, fill=pepper_green
    )
    
    y_position += brand_bbox[3] - brand_bbox[1] + int(target_height_px * 0.01)
    
    # Subtitle
    subtitle = "APARTMENTS"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_medium)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    
    draw.text(
        (tree_center_x - subtitle_width / 2, y_position),
        subtitle, font=font_medium, fill=dark_brown
    )
    
    print("→ Placed brand name with traditional typography")

    # --- 6. Primary Message: "FOR RENT" Banner ---
    y_position += subtitle_bbox[3] + int(target_height_px * 0.06)
    
    # Create a green banner across the sign
    banner_height = int(target_height_px * 0.20)
    banner_margin = int(target_width_px * 0.08)
    
    # Banner background with rounded ends
    draw.rounded_rectangle(
        [(banner_margin, y_position),
         (target_width_px - banner_margin, y_position + banner_height)],
        radius=int(banner_height * 0.15),
        fill=pepper_green
    )
    
    # "FOR RENT" text on banner
    rent_text = "FOR RENT"
    rent_bbox = draw.textbbox((0, 0), rent_text, font=font_headline)
    rent_width = rent_bbox[2] - rent_bbox[0]
    rent_height = rent_bbox[3] - rent_bbox[1]
    
    text_y = y_position + (banner_height - rent_height) / 2
    draw.text(
        (tree_center_x - rent_width / 2, text_y),
        rent_text, font=font_headline, fill=cream_background
    )
    
    print("→ Created prominent FOR RENT banner")

    # --- 7. Unit Details & Phone Number ---
    y_position += banner_height + int(target_height_px * 0.06)
    
    # Unit type
    unit_text = "3 Bedroom / 2.5 Bath Townhomes"
    unit_bbox = draw.textbbox((0, 0), unit_text, font=font_medium)
    unit_width = unit_bbox[2] - unit_bbox[0]
    
    draw.text(
        (tree_center_x - unit_width / 2, y_position),
        unit_text, font=font_medium, fill=pepper_green
    )
    
    y_position += unit_bbox[3] + int(target_height_px * 0.04)
    
    # Special offer
    special_text = "★  MOVE-IN SPECIALS AVAILABLE  ★"
    special_bbox = draw.textbbox((0, 0), special_text, font=font_medium)
    special_width = special_bbox[2] - special_bbox[0]
    
    draw.text(
        (tree_center_x - special_width / 2, y_position),
        special_text, font=font_medium, fill=dark_brown
    )
    
    y_position += special_bbox[3] + int(target_height_px * 0.05)
    
    # Phone number - LARGE and prominent
    phone_text = "(559) 935-2985"
    phone_bbox = draw.textbbox((0, 0), phone_text, font=font_large)
    phone_width = phone_bbox[2] - phone_bbox[0]
    phone_height = phone_bbox[3] - phone_bbox[1]
    
    # Phone number box
    phone_box_padding = int(target_height_px * 0.025)
    draw.rounded_rectangle(
        [(tree_center_x - phone_width / 2 - phone_box_padding, y_position - phone_box_padding),
         (tree_center_x + phone_width / 2 + phone_box_padding, y_position + phone_height + phone_box_padding)],
        radius=15,
        fill=white,
        outline=pepper_green,
        width=int(border_width * 0.8)
    )
    
    draw.text(
        (tree_center_x - phone_width / 2, y_position),
        phone_text, font=font_large, fill=pepper_green
    )
    
    print("→ Added unit details and call-to-action")

    # --- 8. Footer Information ---
    footer_y = int(target_height_px * 0.92)
    
    footer_text = "PROFESSIONALLY MANAGED  •  AVAILABLE NOW"
    footer_bbox = draw.textbbox((0, 0), footer_text, font=font_small)
    footer_width = footer_bbox[2] - footer_bbox[0]
    
    draw.text(
        (tree_center_x - footer_width / 2, footer_y),
        footer_text, font=font_small, fill=dark_brown
    )
    
    # --- 9. Save Final Sign ---
    try:
        img.save(output_path, "JPEG", quality=98, dpi=(dpi, dpi), optimize=True)
        print(f"✓ SUCCESS: Brand-authentic sign saved to '{output_path}'")
        print(f"  Matches Pepper Tree's established visual identity")
    except Exception as e:
        print(f"✗ ERROR: {e}")

if __name__ == "__main__":
    create_brand_authentic_sign(
        output_path=os.path.join("images", "for_rent_sign_brand_authentic_8x4.jpg"),
        banner_width_ft=8,
        banner_height_ft=4,
        dpi=150
    )
