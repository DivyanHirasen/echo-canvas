import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

ADD_SHADOW = False
SHADOW_DEPTH = 5

def add_quote_to_image(image_path: str, quote: str, output_path: str = None) -> str:
    """Overlays a quote onto an image and saves it."""
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size

    # Semi-transparent dark overlay for readability
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle([(0, height * 0.55), (width, height)], fill=(0, 0, 0, 80))
    img = Image.alpha_composite(img, overlay).convert("RGB")

    draw = ImageDraw.Draw(img)

    # Font sizing relative to image width
    font_size = max(28, width // 22)
    # font_paths = [
    #     "/System/Library/Fonts/Palatino.ttc",
    #     "/System/Library/Fonts/Optima.ttc",
    #     "/System/Library/Fonts/SFGeorgian.ttf",
    # ]
    # font = ImageFont.load_default()
    # for path in font_paths:
    #     try:
    #         font = ImageFont.truetype(path, font_size)
    #         break
    #     except OSError:
    #         continue

    font_path = "fonts/LacheyardScript_PERSONAL_USE_ONLY.otf"
    font_path = "fonts/Qafinte.otf"
    font_path = "fonts/LongaIberica-DEMO.ttf"
    font_path = "fonts/Bassy.ttf"
    
    font = ImageFont.truetype(font_path, font_size)

    # Wrap text to fit image width
    max_chars = int(width / (font_size * 0.55))
    lines = textwrap.wrap(quote, width=max_chars)
    line_height = font_size + 14
    total_text_height = len(lines) * line_height

    # Center text in the lower portion
    y = int(height * 0.6) + (int(height * 0.35) - total_text_height) // 2

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        # Soft multi-layer shadow
        # for offset in range(1, 5):
        #     draw.text((x + offset, y + offset), line, font=font, fill=(0, 0, 0, 60))
        # Main text
        draw.text((x, y), line, font=font, fill=(255, 250, 240, 255))
        y += line_height

    if output_path is None:
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_quote{ext}"

    img.save(output_path)
    print(f"Quote image saved to: {output_path}")
    return output_path
