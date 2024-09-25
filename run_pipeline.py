# Penggunaan pipeline
from pipeline.yolo_video_to_sequence_pipeline import yolo_process_video_pipeline
from pipeline.pacal_voc_xml_video_to_sequence_pipeline import xml_process_video_pipeline
from pipeline.coco_json_video_to_sequence_pipeline import coco_json_process_video_pipeline

import os

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-COCO' # Change this
VIDEO_NAME = '4K Video of Highway Traffic! (online-video-cutter.com).mp4' # Change this
FILE_NAMES = '_instances_default.json'

BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
VIDEO_PATH = os.path.join(BASE_DIR, VIDEO_NAME)

# yolo_process_video_pipeline(PROJECT_PATH, VIDEO_PATH, FILE_NAMES, PROJECT_NAME)
# xml_process_video_pipeline(PROJECT_PATH, VIDEO_PATH, FILE_NAMES)
coco_json_process_video_pipeline(PROJECT_PATH, FILE_NAMES, VIDEO_PATH, is_split=True, random_split=True, split_ratio=0.9)