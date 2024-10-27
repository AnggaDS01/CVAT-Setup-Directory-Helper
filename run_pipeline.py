# Penggunaan pipeline
# from src.pipeline.pacal_voc_xml_video_to_sequence_pipeline import xml_process_video_pipeline
# from src.pipeline.coco_json_video_to_sequence_pipeline import coco_json_process_video_pipeline

from src.pipeline.yolo_pipeline import yolo_pipeline_format_processor
from control_panel import *

yolo_pipeline_format_processor(
    source_path=VIDEO_TARGET_NAME_PATH, 
    fps=FPS, 
    images_ext=EXT, 
    image_size=IMAGE_SIZE, 
    split_ratio=SPLIT_RATIO, 
    random_split=RANDOM_SPLIT,
    seed=SEED, 
)

# xml_process_video_pipeline(
#     project_path=PROJECT_PATH, 
#     source_filename=FILE_NAMES, 
#     video_path=VIDEO_PATH, 
#     split_ratio=SPLIT_RATIO, 
#     random_split=RANDOM_SPLIT,
#     seed=SEED,
#     is_split=IS_SPLIT,
#     ext=EXT
# )

# coco_json_process_video_pipeline(
#     project_path=PROJECT_PATH, 
#     coco_json_filename=FILE_NAMES, 
#     video_path=VIDEO_PATH, 
#     split_ratio=SPLIT_RATIO,
#     random_split=RANDOM_SPLIT, 
#     is_split=IS_SPLIT, 
#     seed=SEED,
#     ext=EXT
# )