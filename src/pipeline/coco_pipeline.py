from src.components.video_to_frames import extract_frames_from_video
from src.components.target_store_directory import get_annotated_target_dir
from src.components.coco_src.coco_setup_directory_structure import coco_setup_directory_structure
from src.components.coco_src.coco_splitter import coco_split_dataset
from src.constants import *

from pathlib import Path

def coco_pipeline_format_processor(
        source_path, 
        fps, 
        images_ext, 
        image_size, 
        split_ratio, 
        random_split,
        seed,
    ) -> None:

    """
    Pipeline for COCO format.

    This function processes the source path and its content according to the chosen format
    for object detection datasets. It supports COCO format.

    Parameters:
        source_path (Path): The path to the source directory containing videos or images.
        fps (int): Frames per second to extract from videos.
        images_ext (str): The file extension for images.
        image_size (tuple): The desired size for the output images.
        split_ratio (tuple): The ratio for splitting the dataset (e.g., (0.8, 0.1) for train and validation).
        random_split (bool): Whether to randomly split the dataset.
        seed (int): Seed for random splitting.

    Returns:
        None
    """
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
        input_images_dir=ANNOTATED_TARGET_DIR_PATH,
        is_video=bool(VIDEO_EXTENSIONS_PATTERN.search(str(source_path))),
        image_size=image_size
    )

    # 3. split dataset
    coco_split_dataset(
        input_images_dir=ANNOTATED_TARGET_DIR_PATH, 
        split_ratio=split_ratio,
        random_split=random_split, 
        seed=seed
    )