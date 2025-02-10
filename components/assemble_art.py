from PIL import Image, ImageDraw
from config import BACKGROUND_PATH, FINAL_ART_PATH, get_word_image_path

# Load background
try:
    background = Image.open(BACKGROUND_PATH)
    print("Background image loaded successfully.")
except FileNotFoundError:
    print("Error: 'background.png' not found. Please check the file path.")
    exit()

# Define positions (adjust these coordinates as needed)
word_positions = {
    "Spanish": (200, 500),
    "Arabic": (1000, 300),
    "Japanese": (800, 1200),
    "Chinese": (400, 700),
}

# Paste each word onto the background
for lang, pos in word_positions.items():
    try:
        # Load the word image
        word_img_path = get_word_image_path(lang)
        word_img = Image.open(word_img_path)
        print(f"Loaded {word_img_path} successfully.")

        # Resize if needed
        word_img = word_img.resize((400, 400))

        # Ensure the word image has an alpha channel (transparency)
        if word_img.mode != "RGBA":
            word_img = word_img.convert("RGBA")

        # Paste the word image onto the background
        background.paste(word_img, pos, mask=word_img)
    except FileNotFoundError:
        print(f"Error: {word_img_path} not found. Skipping this language.")
    except Exception as e:
        print(f"Error processing {word_img_path}: {e}")

background.save(FINAL_ART_PATH)