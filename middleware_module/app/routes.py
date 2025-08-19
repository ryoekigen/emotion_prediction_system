from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil
import uuid
from app import result_manager, openface_client

router = APIRouter()

DATA_ROOT = Path("/openface-data")

@router.post("/process/")
async def process_video(user_id: str, file: UploadFile = File(...)):
    """Receive a video, save it to shared volume, trigger OpenFace"""
    video_id = str(uuid.uuid4())
    input_path = result_manager.save_video(user_id, video_id, file)

    # Call OpenFace processing (async or trigger)
    openface_client.run_openface(user_id, video_id, input_path)

    return {"user_id": user_id, "video_id": video_id, "status": "processing started"}


@router.get("/status/{user_id}/{video_id}")
async def check_status(user_id: str, video_id: str):
    """Check processing status"""
    status = result_manager.check_status(user_id, video_id)
    return {"user_id": user_id, "video_id": video_id, "status": status}


@router.get("/result/{user_id}/{video_id}")
async def get_result(user_id: str, video_id: str):
    """Fetch final result JSON if exists"""
    result = result_manager.get_result(user_id, video_id)
    if not result:
        raise HTTPException(status_code=404, detail="Result not ready")
    return result
