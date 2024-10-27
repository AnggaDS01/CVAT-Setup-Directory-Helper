from src.components.video_to_frames import extract_frames_from_video
from src.components.yolo_src.yolo_setup_directory_structure import yolo_setup_directory_structure
from src.components.yolo_src.yolo_splitter import yolo_split_dataset
from src.components.target_store_directory import get_annotated_target_dir
from src.constants import *

# Pipeline for yolo
def yolo_pipeline_format_processor(
        source_path, 
        fps, 
        images_ext, 
        image_size, 
        split_ratio, 
        random_split,
        seed,
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
    yolo_setup_directory_structure(
        input_images_dir=ANNOTATED_TARGET_DIR_PATH,
        is_video=bool(VIDEO_EXTENSIONS_PATTERN.search(str(source_path))),
        image_size=image_size
    )
    
    # 3. split dataset
    yolo_split_dataset(
        images_labels_dir_path=ANNOTATED_TARGET_DIR_PATH, 
        split_ratio=split_ratio,
        random_split=random_split, 
        seed=seed
    )