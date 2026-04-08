from diffusers import DiffusionPipeline
import torch

pipe = None

def load_model():
    global pipe
    if pipe is None:
        pipe = DiffusionPipeline.from_pretrained(
            "/workspace/models/flux",
            torch_dtype=torch.float16
        ).to("cuda")

def generate_image(prompt):
    load_model()
    image = pipe(prompt).images[0]

    path = "/tmp/output.png"
    image.save(path)

    return path