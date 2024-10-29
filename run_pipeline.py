from src.pipeline.cvat_setup_directory_pipeline import setup_dir_pipeline
from control_panel import *

if __name__ == "__main__":
    setup_dir_pipeline(
        format_output='coco',
        source_path=IMAGES_TARGET_DIR_PATH, 
        fps=FPS,
        images_ext=EXT, 
        image_size=IMAGE_SIZE, 
        split_ratio=SPLIT_RATIO, 
        random_split=RANDOM_SPLIT,
        seed=SEED, 
    )