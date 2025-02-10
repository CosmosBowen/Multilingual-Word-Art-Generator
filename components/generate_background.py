from PIL import Image, ImageDraw
import random
from config import BACKGROUND_PATH

# Create a blank canvas
width, height = 2000, 2000
background = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(background)

# Add random colorful circles
for _ in range(100):
    x, y = random.randint(0, width), random.randint(0, height)
    radius = random.randint(50, 200)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.ellipse([x, y, x + radius, y + radius], fill=color, outline=None)

background.save(BACKGROUND_PATH)
