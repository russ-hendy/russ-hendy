import os
from PIL import Image
import random
from collections import Counter

def generate_texture():
    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, 'bauhaus-bg.png')
    output_path = os.path.join(base_dir, 'bauhaus-bg-generated.png')

    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    # 1. Load and Downscale
    # "Compress down by 75%" -> Resize to 25% of original size
    # This averages out the "cross-hatch" into cleaner dominant colors
    original = Image.open(input_path).convert('RGB')
    w, h = original.size
    
    # Scale factor 0.25 (25% size)
    small_w, small_h = int(w * 0.25), int(h * 0.25)
    print(f"Resizing original ({w}x{h}) to ({small_w}x{small_h})...")
    
    # Use BOX or BILINEAR to average pixels
    small_img = original.resize((small_w, small_h), resample=Image.Resampling.BOX)

    # 2. Extract Color Palette (Quantization)
    # We want "4 different colors"
    # P is palettized. ADAPTIVE tries to find best 4 colors.
    quantized_img = small_img.quantize(colors=4)
    # Convert back to RGB to get values
    quantized_rgb = quantized_img.convert('RGB')
    
    # Count frequency of each of the 4 colors to calculate distribution
    pixels = list(quantized_rgb.getdata())
    color_counts = Counter(pixels)
    total_pixels = len(pixels)
    
    # ... (Previous quantization code remains similar, but we extract the palette)
    print("Dominant Colors Found:")
    taxonomy = []
    for color, count in color_counts.most_common():
        prob = count / total_pixels
        taxonomy.append((color, prob))
        print(f"  Color: {color}, Probability: {prob:.3f}")

    # Helper: Contrast Stretcher
    def increase_contrast(palette, factor=1.5):
        # Calculate mean luminance
        def lum(c): return 0.299*c[0] + 0.587*c[1] + 0.114*c[2]
        avg_lum = sum(lum(c) for c in palette) / len(palette)
        
        new_palette = []
        for c in palette:
            # Shift away from avg
            l = lum(c)
            diff = l - avg_lum
            # Amplify difference
            r = int(max(0, min(255, c[0] + (c[0]-avg_lum)*0.5))) # Simple component stretch
            g = int(max(0, min(255, c[1] + (c[1]-avg_lum)*0.5)))
            b = int(max(0, min(255, c[2] + (c[2]-avg_lum)*0.5)))
            
            # Simple clamping doesn't preserve hue well, strictly speaking, 
            # but for "tea stains" (monochromaticish) it works to separate values.
            # Let's just pull 'darkest' darker and 'lightest' lighter manually for safety?
            # Actually, standard contrast algorithm per channel:
            # color = (color - 128) * factor + 128. But relative to average is better.
            new_palette.append((r, g, b))
        return new_palette

    basic_colors = [t[0] for t in taxonomy]
    weights = [t[1] for t in taxonomy]
    contrast_colors = increase_contrast(basic_colors)

    def save_variant(name, colors, pixel_scale=1):
        gen_w = 256 // pixel_scale
        gen_h = 256 // pixel_scale
        img = Image.new('RGB', (gen_w, gen_h))
        data = random.choices(colors, weights=weights, k=gen_w*gen_h)
        img.putdata(data)
        
        if pixel_scale > 1:
            img = img.resize((256, 256), resample=Image.Resampling.NEAREST)
            
        out = os.path.join(base_dir, f'bauhaus-bg-{name}.png')
        img.save(out)
        print(f"Saved {out}")

    # Generate Variants
    save_variant('contrast', contrast_colors, pixel_scale=1)
    save_variant('coarse', basic_colors, pixel_scale=2)
    save_variant('hybrid', contrast_colors, pixel_scale=2)

if __name__ == "__main__":
    generate_texture()
