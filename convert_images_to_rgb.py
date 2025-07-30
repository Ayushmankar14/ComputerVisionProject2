from PIL import Image
import os

input_folder = "images"           # Where original photos are
output_folder = "known_faces"     # Final folder for RGB-encoded images

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    try:
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp")):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                print(f"[🧾] {filename} original mode: {img.mode}")

                # Convert image to standard RGB format (8-bit, no alpha)
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new("RGB", img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])  # Alpha channel as mask
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert("RGB")

                output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
                img.save(output_path, format="JPEG", quality=95)
                print(f"[✅] Converted and saved: {filename} -> {output_path}")
    except Exception as e:
        print(f"[❌] Error converting {filename}: {e}")
