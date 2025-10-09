from PIL import Image, ImageDraw, ImageFont
import os

def create_for_rent_banner():
    """
    Generates a 'For Rent' banner for PepperTree Townhomes.
    """
    # --- 1. Configuration ---
    width, height = 1200, 600
    output_path = os.path.join("images", "for_rent_banner.jpg")
    background_image_path = os.path.join("images", "760_Outside.jpg")

    # Colors from the website's CSS
    primary_color = "#2c5f2d"
    secondary_color = "#97be5a"
    white_color = "#ffffff"
    text_dark = "#333333"

    # --- 2. Create Base Image ---
    # Open the background image and resize it
    try:
        background = Image.open(background_image_path)
        # Crop the image to the desired aspect ratio before resizing
        bg_width, bg_height = background.size
        target_aspect = width / height
        current_aspect = bg_width / bg_height

        if current_aspect > target_aspect:
            # Background is wider than target, crop width
            new_width = int(target_aspect * bg_height)
            left = (bg_width - new_width) / 2
            right = (bg_width + new_width) / 2
            background = background.crop((left, 0, right, bg_height))
        else:
            # Background is taller than target, crop height
            new_height = int(bg_width / target_aspect)
            top = (bg_height - new_height) / 2
            bottom = (bg_height + new_height) / 2
            background = background.crop((0, top, bg_width, bottom))
        
        background = background.resize((width, height), Image.LANCZOS)
    except FileNotFoundError:
        print(f"Background image not found at {background_image_path}. Creating a plain green background.")
        background = Image.new("RGB", (width, height), primary_color)

    # Create a drawing context
    draw = ImageDraw.Draw(background, "RGBA")

    # --- 3. Add a Darkening Overlay for Text Legibility ---
    overlay_color = (44, 95, 45, 200) # primary_color with ~80% opacity
    draw.rectangle([(0, 0), (width, height)], fill=overlay_color)

    # --- 4. Prepare Fonts ---
    # Using a common system font. If not available, Pillow uses a default.
    try:
        font_bold_path = "arialbd.ttf" # Arial Bold
        font_regular_path = "arial.ttf" # Arial Regular
        font_large = ImageFont.truetype(font_bold_path, 150)
        font_medium = ImageFont.truetype(font_bold_path, 60)
        font_small = ImageFont.truetype(font_regular_path, 36)
        font_contact = ImageFont.truetype(font_regular_path, 32)
    except IOError:
        print("Arial font not found. Using default font.")
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_contact = ImageFont.load_default()

    # --- 5. Add Text Elements ---
    
    # Main "FOR RENT" headline
    for_rent_text = "FOR RENT"
    text_width, text_height = draw.textbbox((0, 0), for_rent_text, font=font_large)[2:4]
    draw.text(((width - text_width) / 2, 80), for_rent_text, font=font_large, fill=white_color)

    # Property Name
    property_text = "PepperTree Townhomes"
    text_width, text_height = draw.textbbox((0, 0), property_text, font=font_medium)[2:4]
    draw.text(((width - text_width) / 2, 260), property_text, font=font_medium, fill=secondary_color)

    # Sub-headline
    sub_headline = "Spacious 2 & 3 Bedroom Homes Available Now"
    text_width, text_height = draw.textbbox((0, 0), sub_headline, font=font_small)[2:4]
    draw.text(((width - text_width) / 2, 350), sub_headline, font=font_small, fill=white_color)

    # Contact Info
    phone_text = "Call: (555) 555-1234"
    website_text = "Visit: peppertreetownhomes.com"
    
    # Draw a semi-transparent white bar for the contact info
    draw.rectangle([(0, height - 100), (width, height)], fill=(255, 255, 255, 220))

    # Phone text
    text_width, text_height = draw.textbbox((0, 0), phone_text, font=font_contact)[2:4]
    draw.text(((width / 2) - text_width - 50, height - 80), phone_text, font=font_contact, fill=text_dark)
    
    # Website text
    text_width, text_height = draw.textbbox((0, 0), website_text, font=font_contact)[2:4]
    draw.text(((width / 2) + 50, height - 80), website_text, font=font_contact, fill=text_dark)

    # --- 6. Save the Image ---
    # Convert to RGB before saving as JPEG
    if background.mode == 'RGBA':
        background = background.convert('RGB')
        
    background.save(output_path, "JPEG", quality=95)
    print(f"Banner saved successfully to {output_path}")

if __name__ == "__main__":
    create_for_rent_banner()
