from src.components.video_to_frames import extract_frames_from_video
from src.components.target_store_directory import get_annotated_target_dir
from src.components.coco_src.coco_splitter import coco_split_dataset
from src.components.coco_src.coco_setup_directory_structure import coco_setup_directory_structure
from src.constants import *

from pathlib import Path
import os

# Pipeline utama untuk menjalankan proses dari awal hingga akhir
def coco_pipeline_format_processor(
        source_path: Path=None, 
        fps: int=30, 
        images_ext: str='jpg', 
        image_size: tuple=None, 
        split_ratio=None, 
        random_split: bool=True,
        seed: int=42, 
    ) -> None:

    ANNOTATED_TARGET_DIR_PATH = get_annotated_target_dir(source_path)

    # 1. extract frames from video
    if VIDEOS_DIR_NAME in str(source_path):
        extract_frames_from_video(
            video_target_name_path=source_path,
            output_dir_path=ANNOTATED_TARGET_DIR_PATH,
            fps=fps,
            images_ext=images_ext,
            image_size=image_size
        )
    
    # 2. setup directory structure
    coco_setup_directory_structure(
        images_store_dir_path=ANNOTATED_TARGET_DIR_PATH,
        is_video=bool(VIDEO_EXTENSIONS_PATTERN.search(str(source_path))),
        image_size=image_size
    )

    # 3. split dataset
    coco_split_dataset(
        images_labels_dir_path=ANNOTATED_TARGET_DIR_PATH, 
        split_ratio=split_ratio,
        random_split=random_split, 
        seed=seed
    )