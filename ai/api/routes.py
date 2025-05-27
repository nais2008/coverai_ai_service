from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from services.generation_service import generate_from_video_and_text

router = APIRouter()

@router.post("/api/v1/generate")
async def generate(text: str = Form(...), video: UploadFile = File(...)):
    video_bytes = await video.read()
    image_url = generate_from_video_and_text(video_bytes, text)
    return JSONResponse({"status": "success", "image_url": image_url})
