import torch
from diffusers import StableDiffusionPipeline
from config import get_word_image_path, PROMPTS

device = "mps" if torch.backends.mps.is_available() else "cpu"
dtype = torch.float32

# Load Stable Diffusion pipeline
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=dtype)
pipe = pipe.to(device)

# Generate images
for lang, prompt in PROMPTS.items():
    image = pipe(prompt, height=512, width=512).images[0]
    image.save(get_word_image_path(lang))