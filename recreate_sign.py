from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import os

def create_inspired_sign(output_path, banner_width_ft, banner_height_ft, dpi):
    """
    Designs and generates a high-resolution 'For Rent' sign inspired by the user-provided image.
    """
    print("--- Inspired 'For Rent' Sign Designer ---")

    # --- 1. Configuration ---
    # Dimensions
    target_width_px = int(banner_width_ft * 12 * dpi)
    target_height_px = int(banner_height_ft * 12 * dpi)
    
    # Colors from inspiration image
    parchment_bg = "#f3e9d8"
    maroon_text = "#8B0000"
    dark_green_text = "#2c5f2d"
    brown_text = "#6b4f4b"
    
    # Text Content
    special_text = "Move In Special"
    main_headline = "PepperTree"
    sub_headline = "TOWNHOMES"
    phone_number = "(559) 935-2985"
    for_rent_text = "FOR RENT"

    # --- 2. Create Base Image ---
    print(f"Creating a {target_width_px}x{target_height_px} canvas.")
    img = Image.new("RGB", (target_width_px, target_height_px), parchment_bg)
    draw = ImageDraw.Draw(img)

    # --- 3. Create Stylized Building Illustration ---
    try:
        building_photo_path = os.path.join("images", "730_750_Outside2.jpg")
        building_photo = Image.open(building_photo_path)
        
        # Convert to grayscale and find edges to create a line-art effect
        line_art = building_photo.convert("L")
        line_art = line_art.filter(ImageFilter.FIND_EDGES)
        line_art = line_art.filter(ImageFilter.SMOOTH_MORE)
        line_art = ImageOps.invert(line_art) # Invert to get dark lines on a light background
        line_art = line_art.convert("RGBA")

        # Make the background transparent
        datas = line_art.getdata()
        newData = []
        for item in datas:
            if item[0] < 200 and item[1] < 200 and item[2] < 200: # if pixel is not white
                newData.append((44, 95, 45, 255)) # Change color to dark green
            else:
                newData.append((255, 255, 255, 0)) # Make white transparent
        line_art.putdata(newData)

        # Resize and place on the right side of the banner
        art_width = int(target_width_px * 0.55)
        art_height = int(art_width / (building_photo.width / building_photo.height))
        line_art = line_art.resize((art_width, art_height), Image.LANCZOS)
        
        img.paste(line_art, (target_width_px - art_width - int(target_width_px * 0.02), 
                             (target_height_px - art_height) // 2), line_art)
        print("Successfully created and placed stylized building art.")
    except Exception as e:
        print(f"Could not create building illustration: {e}")

    # --- 4. Prepare Fonts ---
    try:
        font_serif_italic = ImageFont.truetype("georgiai.ttf", int(target_height_px * 0.1))
        font_serif_decorative = ImageFont.truetype("georgia.ttf", int(target_height_px * 0.12))
        font_sans_condensed = ImageFont.truetype("arial.ttf", int(target_height_px * 0.05))
        font_sans_bold = ImageFont.truetype("arialbd.ttf", int(target_height_px * 0.1))
        font_sans_block = ImageFont.truetype("arialbd.ttf", int(target_height_px * 0.18))
    except IOError:
        print("Using default fonts as specific ones were not found.")
        font_serif_italic = ImageFont.load_default()
        font_serif_decorative = ImageFont.load_default()
        font_sans_condensed = ImageFont.load_default()
        font_sans_bold = ImageFont.load_default()
        font_sans_block = ImageFont.load_default()

    # --- 5. Draw Text Elements (Left Column) ---
    left_margin = int(target_width_px * 0.05)

    # "Move In Special"
    draw.text((left_margin, int(target_height_px * 0.1)), special_text, font=font_serif_italic, fill=maroon_text)

    # "PepperTree"
    draw.text((left_margin, int(target_height_px * 0.25)), main_headline, font=font_serif_decorative, fill=dark_green_text)

    # "TOWNHOMES"
    draw.text((left_margin, int(target_height_px * 0.4)), sub_headline, font=font_sans_condensed, fill=dark_green_text)

    # Phone Number
    draw.text((left_margin, int(target_height_px * 0.5)), phone_number, font=font_sans_bold, fill=dark_green_text)

    # "FOR RENT"
    draw.text((left_margin, int(target_height_px * 0.68)), for_rent_text, font=font_sans_block, fill=brown_text)
    
    # --- 6. Add Border ---
    border_width = int(target_width_px * 0.005)
    draw.rectangle([(0,0), (target_width_px-1, target_height_px-1)], outline="#c9b89c", width=border_width)

    # --- 7. Save the Final Image ---
    try:
        img.save(output_path, "JPEG", quality=95, dpi=(dpi, dpi))
        print(f"SUCCESS: New sign saved to '{output_path}'")
    except Exception as e:
        print(f"ERROR: Failed to save the image. {e}")

if __name__ == "__main__":
    create_inspired_sign(
        output_path=os.path.join("images", "for_rent_sign_inspired_8x4.jpg"),
        banner_width_ft=8,
        banner_height_ft=4,
        dpi=150
    )
