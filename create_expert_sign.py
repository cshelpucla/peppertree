from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import numpy as np

def create_expert_sign(inspiration_image_path, output_path, banner_width_ft, banner_height_ft, dpi):
    """
    Designs and generates a high-resolution 'For Rent' sign with expert design principles.
    """
    print("--- Expert Sign Designer ---")

    # --- 1. Refined Configuration ---
    target_width_px = int(banner_width_ft * 12 * dpi)
    target_height_px = int(banner_height_ft * 12 * dpi)
    
    # Professional Color Palette
    parchment_bg = "#f5efe1"
    maroon_text = "#800000"
    dark_green_text = "#004d00"
    brown_text = "#5d4037"
    gold_accent = "#c9b89c"

    # Text Content
    special_text = "Move In Special"
    main_headline = "PepperTree"
    sub_headline = "TOWNHOMES"
    phone_number = "(559) 935-2985"
    for_rent_text = "FOR RENT"

    # --- 2. Create High-Quality Canvas with Texture ---
    print("Creating a textured, high-resolution canvas.")
    img = Image.new("RGB", (target_width_px, target_height_px), parchment_bg)
    
    # Add subtle noise for a textured paper feel
    noise = np.random.randint(-5, 5, (target_height_px, target_width_px, 3), dtype=np.int16)
    img_array = np.array(img, dtype=np.int16) + noise
    img_array = np.clip(img_array, 0, 255)
    img = Image.fromarray(img_array.astype(np.uint8))

    # --- 3. Load and Prepare Graphical Elements ---
    try:
        inspiration_img = Image.open(inspiration_image_path).convert("RGBA")
    except FileNotFoundError:
        print(f"ERROR: Inspiration image not found.")
        return

    tree_element = inspiration_img.crop((15, 40, 145, 215))
    building_element = inspiration_img.crop((410, 20, 830, 230))
    print("Extracted graphical elements.")

    # --- 4. Compose Layout with Balance and Depth ---
    
    # Create a separate layer for shadows
    shadow_layer = Image.new('RGBA', img.size, (0,0,0,0))
    shadow_draw = ImageDraw.Draw(shadow_layer)

    # Place Building with Shadow
    building_aspect = building_element.width / building_element.height
    building_width = int(target_width_px * 0.5)
    building_height = int(building_width / building_aspect)
    building_resized = building_element.resize((building_width, building_height), Image.LANCZOS)
    building_x = target_width_px - building_width - int(target_width_px * 0.04)
    building_y = (target_height_px - building_height) // 2
    
    shadow_offset = int(target_width_px * 0.005)
    shadow_draw.bitmap((building_x + shadow_offset, building_y + shadow_offset), building_resized, fill=(0,0,0,80))
    img.paste(building_resized, (building_x, building_y), building_resized)
    print("Composited building element with drop shadow.")

    # Place Tree with Shadow
    tree_aspect = tree_element.width / tree_element.height
    tree_height = int(target_height_px * 0.65)
    tree_width = int(tree_height * tree_aspect)
    tree_resized = tree_element.resize((tree_width, tree_height), Image.LANCZOS)
    tree_x = int(target_width_px * 0.04)
    tree_y = (target_height_px - tree_height) // 2

    shadow_draw.bitmap((tree_x + shadow_offset, tree_y + shadow_offset), tree_resized, fill=(0,0,0,80))
    img.paste(tree_resized, (tree_x, tree_y), tree_resized)
    print("Composited tree element with drop shadow.")

    # Blur the shadow layer and composite it
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=shadow_offset / 2))
    img = Image.alpha_composite(img.convert("RGBA"), shadow_layer).convert("RGB")
    
    # --- 5. Apply Expert Typography ---
    draw = ImageDraw.Draw(img)
    try:
        font_serif_special = ImageFont.truetype("georgiai.ttf", int(target_height_px * 0.11))
        font_serif_main = ImageFont.truetype("georgia.ttf", int(target_height_px * 0.13))
        font_sans_sub = ImageFont.truetype("arial.ttf", int(target_height_px * 0.05))
        font_sans_phone = ImageFont.truetype("arialbd.ttf", int(target_height_px * 0.1))
        font_sans_rent = ImageFont.truetype("arialbd.ttf", int(target_height_px * 0.2))
    except IOError:
        print("Using default fonts.")
        # Fallback fonts
        font_serif_special, font_serif_main, font_sans_sub, font_sans_phone, font_sans_rent = (ImageFont.load_default(),)*5

    text_left_margin = int(target_width_px * 0.23)
    
    # Function to draw text with a subtle shadow for readability
    def draw_text_with_shadow(pos, text, font, fill, shadow_fill=(0,0,0,50)):
        x, y = pos
        offset = int(font.size * 0.03)
        draw.text((x + offset, y + offset), text, font=font, fill=shadow_fill)
        draw.text((x, y), text, font=font, fill=fill)

    draw_text_with_shadow((text_left_margin, int(target_height_px * 0.08)), special_text, font_serif_special, maroon_text)
    draw_text_with_shadow((text_left_margin, int(target_height_px * 0.22)), main_headline, font_serif_main, dark_green_text)
    draw.text((text_left_margin, int(target_height_px * 0.38)), sub_headline, font=font_sans_sub, fill=dark_green_text)
    draw_text_with_shadow((text_left_margin, int(target_height_px * 0.48)), phone_number, font_sans_phone, dark_green_text)
    draw_text_with_shadow((text_left_margin, int(target_height_px * 0.65)), for_rent_text, font_sans_rent, brown_text)
    print("Applied professional typography with depth.")

    # --- 6. Add Final Framing ---
    border_width = int(target_width_px * 0.008)
    draw.rectangle([(0,0), (target_width_px-1, target_height_px-1)], outline=gold_accent, width=border_width)
    inner_border_width = int(border_width * 0.3)
    draw.rectangle([(border_width, border_width), (target_width_px - border_width - 1, target_height_px - border_width - 1)], 
                   outline=parchment_bg, width=inner_border_width)

    # --- 7. Save Final Product ---
    try:
        img.save(output_path, "JPEG", quality=95, dpi=(dpi, dpi))
        print(f"SUCCESS: Expertly designed sign saved to '{output_path}'")
    except Exception as e:
        print(f"ERROR: Failed to save the image. {e}")

if __name__ == "__main__":
    create_expert_sign(
        inspiration_image_path="images/IMG_3858.png",
        output_path=os.path.join("images", "for_rent_sign_expert_8x4.jpg"),
        banner_width_ft=8,
        banner_height_ft=4,
        dpi=150
    )
