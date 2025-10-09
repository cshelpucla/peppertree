from PIL import Image, ImageDraw, ImageFont
import os

def create_final_sign(inspiration_image_path, output_path, banner_width_ft, banner_height_ft, dpi):
    """
    Recreates the banner using graphical elements cropped from the user's inspiration image.
    """
    print("--- Final Sign Creator (using provided elements) ---")

    # --- 1. Configuration ---
    target_width_px = int(banner_width_ft * 12 * dpi)
    target_height_px = int(banner_height_ft * 12 * dpi)
    
    # Colors and text from inspiration
    parchment_bg = "#f3e9d8"
    maroon_text = "#8B0000"
    dark_green_text = "#2c5f2d"
    brown_text = "#6b4f4b"
    
    special_text = "Move In Special"
    main_headline = "PepperTree"
    sub_headline = "TOWNHOMES"
    phone_number = "(559) 935-2985"
    for_rent_text = "FOR RENT"

    # --- 2. Load Inspiration Image and Crop Elements ---
    try:
        inspiration_img = Image.open(inspiration_image_path).convert("RGBA")
        print(f"Loaded inspiration image: {inspiration_image_path}")
    except FileNotFoundError:
        print(f"ERROR: Inspiration image not found at '{inspiration_image_path}'.")
        return

    # Define crop boxes (left, top, right, bottom) based on the original 852x250 image
    # Crop the tree
    tree_crop_box = (15, 40, 145, 215)
    tree_element = inspiration_img.crop(tree_crop_box)
    print("Cropped tree element.")

    # Crop the building
    building_crop_box = (410, 20, 830, 230)
    building_element = inspiration_img.crop(building_crop_box)
    print("Cropped building element.")

    # --- 3. Create High-Resolution Canvas ---
    print(f"Creating a {target_width_px}x{target_height_px} canvas.")
    img = Image.new("RGB", (target_width_px, target_height_px), parchment_bg)
    
    # --- 4. Paste and Resize Cropped Elements ---
    
    # Paste Building
    building_aspect = building_element.width / building_element.height
    building_width_hires = int(target_width_px * 0.5)
    building_height_hires = int(building_width_hires / building_aspect)
    building_element_hires = building_element.resize((building_width_hires, building_height_hires), Image.LANCZOS)
    building_x = target_width_px - building_width_hires - int(target_width_px * 0.03)
    building_y = (target_height_px - building_height_hires) // 2
    img.paste(building_element_hires, (building_x, building_y), building_element_hires)
    print("Pasted high-resolution building element.")

    # Paste Tree
    tree_aspect = tree_element.width / tree_element.height
    tree_height_hires = int(target_height_px * 0.6)
    tree_width_hires = int(tree_height_hires * tree_aspect)
    tree_element_hires = tree_element.resize((tree_width_hires, tree_height_hires), Image.LANCZOS)
    tree_x = int(target_width_px * 0.05)
    tree_y = (target_height_px - tree_height_hires) // 2
    img.paste(tree_element_hires, (tree_x, tree_y), tree_element_hires)
    print("Pasted high-resolution tree element.")

    # --- 5. Add Text ---
    draw = ImageDraw.Draw(img)
    try:
        font_serif_italic = ImageFont.truetype("georgiai.ttf", int(target_height_px * 0.1))
        font_serif_decorative = ImageFont.truetype("georgia.ttf", int(target_height_px * 0.12))
        font_sans_condensed = ImageFont.truetype("arial.ttf", int(target_height_px * 0.05))
        font_sans_bold = ImageFont.truetype("arialbd.ttf", int(target_height_px * 0.1))
        font_sans_block = ImageFont.truetype("arialbd.ttf", int(target_height_px * 0.18))
    except IOError:
        print("Using default fonts as specific ones were not found.")
        font_serif_italic, font_serif_decorative, font_sans_condensed, font_sans_bold, font_sans_block = (ImageFont.load_default(),)*5

    text_left_margin = int(target_width_px * 0.22)
    draw.text((text_left_margin, int(target_height_px * 0.1)), special_text, font=font_serif_italic, fill=maroon_text)
    draw.text((text_left_margin, int(target_height_px * 0.25)), main_headline, font=font_serif_decorative, fill=dark_green_text)
    draw.text((text_left_margin, int(target_height_px * 0.4)), sub_headline, font=font_sans_condensed, fill=dark_green_text)
    draw.text((text_left_margin, int(target_height_px * 0.5)), phone_number, font=font_sans_bold, fill=dark_green_text)
    draw.text((text_left_margin, int(target_height_px * 0.68)), for_rent_text, font=font_sans_block, fill=brown_text)
    print("Added all text elements.")

    # --- 6. Add Border ---
    border_width = int(target_width_px * 0.005)
    draw.rectangle([(0,0), (target_width_px-1, target_height_px-1)], outline="#c9b89c", width=border_width)

    # --- 7. Save Final Image ---
    try:
        img.save(output_path, "JPEG", quality=95, dpi=(dpi, dpi))
        print(f"SUCCESS: New sign saved to '{output_path}'")
    except Exception as e:
        print(f"ERROR: Failed to save the image. {e}")

if __name__ == "__main__":
    create_final_sign(
        inspiration_image_path="images/IMG_3858.png", # Assuming the user saved it here
        output_path=os.path.join("images", "for_rent_sign_final_8x4.jpg"),
        banner_width_ft=8,
        banner_height_ft=4,
        dpi=150
    )
