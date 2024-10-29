from src.constants import *

from pathlib import Path
import re

def get_annotated_target_dir(path):
    """
    Checks if the provided path contains the VIDEOS_DIR_NAME, and if so,
    replaces it with ANNOTATED_DIR_NAME and returns the parent directory.

    Args:
        path (Path): The path to be checked and modified.

    Returns:
        Path: The modified path with ANNOTATED_DIR_NAME if VIDEOS_DIR_NAME was found,
        otherwise returns the original path.
    """
    if VIDEOS_DIR_NAME in str(path):
        annotated_path_str = re.sub(rf"({VIDEOS_DIR_NAME})", ANNOTATED_DIR_NAME, str(path))
        return Path(annotated_path_str).parent
    return path