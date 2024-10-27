from src.constants import *

from pathlib import Path
import re

def get_annotated_target_dir(path):
    # Cek apakah path awal mengandung "Videos-Assets", jika ya return dengan .parent
    if VIDEOS_DIR_NAME in str(path):
        # Ganti "Videos-Assets" atau "Images-Assets" dengan "Annotated-Images-Assets"
        annotated_path_str = re.sub(rf"({VIDEOS_DIR_NAME})", ANNOTATED_DIR_NAME, str(path))
        return Path(annotated_path_str).parent
    return path