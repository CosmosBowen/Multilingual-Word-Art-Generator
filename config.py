import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Image paths
IMAGES_DIR = os.path.join(BASE_DIR, "images")
BACKGROUND_PATH = os.path.join(IMAGES_DIR, "background.png")
FINAL_ART_PATH = os.path.join(IMAGES_DIR, "final_art.png")

# Define prompts for each word
PROMPTS = {
    'Spanish': "The single word 'hermosa' in elegant cursive font, floral patterns, vibrant colors, watercolor painting",
    'Arabic': "The single word 'جَمِيلٌ' in gold Arabic calligraphy, intricate islamic geometric patterns, beige background",
    'Japanese': "The single word '美しい' in bold black brushstrokes, minimalist Japanese ink painting, white background",
    'Chinese': "The single word '美丽' in Chinese Lunar New Year Festival's vibes, calligraphy in gold ink and red background",
}


# Word image paths
def get_word_image_path(lang:str):
    return os.path.join(IMAGES_DIR, f"beautiful_{lang}.png")

# print(f"BASE_DIR: {BASE_DIR}")
# print(f"BACKGROUND_PATH: {BACKGROUND_PATH}")
# print(f"FINAL_ART_PATH: {FINAL_ART_PATH}")
# print(f"get_word_image_path: {get_word_image_path("Chinese")}")