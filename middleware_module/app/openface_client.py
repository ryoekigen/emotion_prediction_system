import subprocess
from pathlib import Path

DATA_ROOT = Path("/openface-data")

def run_openface(user_id: str, video_id: str, video_path: Path):
    """Call OpenFace container to process video"""
    output_dir = DATA_ROOT / "openface_output" / user_id / video_id
    output_dir.mkdir(parents=True, exist_ok=True)

    # Example: docker exec or subprocess (adjust to your setup)
    cmd = [
        "docker", "exec", "openface_container",
        "./FeatureExtraction",
        "-f", str(video_path),
        "-out_dir", str(output_dir)
    ]
    subprocess.Popen(cmd)  # run async
