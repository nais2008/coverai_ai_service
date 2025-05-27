from utils.video_utils import extract_frame
from models.sd_model import get_sd_pipeline
import uuid
import os

def generate_from_video_and_text(video_bytes, prompt: str):
    init_image = extract_frame(video_bytes, second=1.0)
    pipe = get_sd_pipeline()

    result = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images[0]

    filename = f"{uuid.uuid4().hex}.jpg"
    path = os.path.join("static", "generated", filename)
    result.save(path)

    return f"/static/generated/{filename}"
