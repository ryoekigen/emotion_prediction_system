from pathlib import Path
import shutil
import json

DATA_ROOT = Path("/openface-data")

def save_video(user_id: str, video_id: str, file) -> Path:
    """Save uploaded video into /video_input/{user_id}/{video_id}/"""
    target_dir = DATA_ROOT / "video_input" / user_id / video_id
    target_dir.mkdir(parents=True, exist_ok=True)

    video_path = target_dir / file.filename
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return video_path


def check_status(user_id: str, video_id: str) -> str:
    """Check whether OpenFace/ML results exist"""
    openface_csv = DATA_ROOT / "openface_output" / user_id / video_id / "features.csv"
    ml_result = DATA_ROOT / "ml_result" / user_id / video_id / "result.json"

    if ml_result.exists():
        return "ml_done"
    elif openface_csv.exists():
        return "openface_done"
    else:
        return "pending"


def get_result(user_id: str, video_id: str):
    """Return ML result JSON if available"""
    result_file = DATA_ROOT / "ml_result" / user_id / video_id / "result.json"
    if result_file.exists():
        with open(result_file, "r") as f:
            return json.load(f)
    return None
